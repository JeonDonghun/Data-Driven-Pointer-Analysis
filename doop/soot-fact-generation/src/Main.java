import java.io.File;
import java.io.OutputStream;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

import soot.ClassProvider;
import soot.Scene;
import soot.SootClass;

public class Main {

    public static enum Mode {INPUTS, FULL;}

  
    private static Mode _mode = null;
    private static List<String> _inputs = new ArrayList<String>();
    private static List<String> _libraries = new ArrayList<String>();
    private static String _outputDir = null;
    private static String _main = null;
    private static boolean _ssa = false;
    private static boolean _trap = false;
    private static boolean _allowPhantom = false;
    private static String appRegex = "**";
  
    private static int shift(String[] args, int index) {
        if(args.length == index + 1) {
            System.err.println("error: option " + args[index] + " requires an argument");
            System.exit(1);
        }

        return index + 1;
    }

    private static boolean isApplicationClass(SootClass klass)
    {        
        for (String pat : appRegex.split(File.pathSeparator))
            if (pat.endsWith(".*")) {
                String pkg = pat.substring(0, pat.length() - 2);
                
                if (klass.getPackageName().equalsIgnoreCase(pkg))
                    return true;
            } else if (pat.endsWith(".**")) {
                String prefix = pat.substring(0, pat.length() - 2);

                if (klass.getName().startsWith(prefix))
                    return true;
            } else if (pat.equals("*") && klass.getPackageName().isEmpty()) {
                return true;
            } else if (pat.equals("**")) {
                return true;
            } else if (klass.getName().equalsIgnoreCase(pat)) {
                return true;
            }
        return false;
    }

    public static void main(String[] args)
    {
        try
        {
            if(args.length == 0) 
            {
                System.err.println("usage: soot-fact-generation [options] file...");
                System.exit(0);
            }

            for(int i = 0; i < args.length; i++)
            {
                if(args[i].equals("--full") || args[i].equals("-full"))
                {
                    if(  _mode != null)
                    { 
                        System.err.println("error: duplicate mode argument");
                        System.exit(1);
                    }

                    _mode = Mode.FULL;
                }
                else if(args[i].equals("-d"))
                {
                    i = shift(args, i);
                    _outputDir = args[i];
                }
                else if(args[i].equals("-main"))
                {
                    i = shift(args, i);
                    _main = args[i];
                }
                else if(args[i].equals("-ssa"))
                {
                    _ssa = true;
                }        
                else if(args[i].equals("-l"))
                {
                    i = shift(args, i);
                    _libraries.add(args[i]);
                }
                else if(args[i].equals("-lsystem") || args[i].equals("--lsystem"))
                {
                    String javaHome = System.getProperty("java.home");
                    _libraries.add(javaHome + File.separator + "lib" + File.separator + "rt.jar");
                    _libraries.add(javaHome + File.separator + "lib" + File.separator + "jce.jar");
                    _libraries.add(javaHome + File.separator + "lib" + File.separator + "jsse.jar");
                }
                else if(args[i].equals("-deps")) {
                    i = shift(args, i);
                    String folderName = args[i];
                    File f = new File(folderName);
                    if(!f.exists()) {
                        System.err.println("Dependency folder " + folderName + " does not exist");
                        System.exit(0);
                    }
                    else if(!f.isDirectory()) {
                        System.err.println("Dependency folder " + folderName + " is not a directory");
                        System.exit(0);
                    }
                    for(File file : f.listFiles()) {
                        if(file.isFile() && file.getName().endsWith(".jar")) {
                            _libraries.add(file.getCanonicalPath());
                        }
                    }
                }
                else if(args[i].equals("-trap"))
                {
                    _trap = true;
                }
                else if(args[i].equals("-application-regex"))
                {
                    i = shift(args, i);
                    appRegex = args[i];
                }        
                else if(args[i].equals("-allow-phantom"))
                {
                    _allowPhantom = true;
                }        
                else if(args[i].equals("-h") || args[i].equals("--help") || args[i].equals("-help")) {
                    System.err.println("usage: soot-fact-generation [options] file...");
                    System.err.println("options:");
                    System.err.println("  -main <class>     Specify the main name of the main class");
                    System.err.println("  -full             Generate facts by full transitive resolution");
                    System.err.println("  -ssa              Generate SSA facts, enabling flow-sensitive analysis");
                    System.err.println("  -d <directory>    Specify where to generate csv fact files.");
                    System.err.println("  -l <archive>      Find classes in jar/zip archive.");
                    System.err.println("  -lsystem          Find classes in default system classes.");
                    System.err.println("  -deps <directory> Add jars in this directory to the class lookup path");
                    System.err.println("  -trap             Generate TRAP files rather than CSV files");
                    System.err.println("  -h, -help,        Print this help message.");
                    System.exit(0);
                }
                else
                {
                    if(args[i].charAt(0) == '-')
                    {
                        System.err.println("error: unrecognized option: " + args[i]);
                        System.exit(0);
                    }
                    else
                    {
                        _inputs.add(args[i]);
                    }
                }
            }

            if(_mode == null) {
                _mode = Mode.INPUTS;
            }

            if(_outputDir == null) {
                _outputDir = System.getProperty("user.dir");
            }

            turnoffSootOutput();

            run();
        }
        catch(Exception exc)
        {
            exc.printStackTrace();
            System.exit(1);
        }
    }

    private static void run() throws Exception
    {
        handleDependence(_main);

        NoSearchingClassProvider provider = new NoSearchingClassProvider();

        for(String arg : _inputs)
        {
            if(arg.endsWith(".jar") || arg.endsWith(".zip"))
            {
                System.out.println("Adding archive: " + arg);
                provider.addArchive(new File(arg));
            }
            else
            {
                System.out.println("Adding file: " + arg);
                provider.addClass(new File(arg));
            }
        }

        for(String lib: _libraries) {
            System.out.println("Adding archive for resolving: " + lib);
            provider.addArchiveForResolving(new File(lib));
        }

        soot.SourceLocator.v().setClassProviders(Collections.singletonList((ClassProvider) provider));
        Scene scene = Scene.v();
        if(_main != null)
        {
            soot.options.Options.v().set_main_class(_main);
        }

        if(_mode == Mode.FULL)
        {
            soot.options.Options.v().set_full_resolver(true);
        }

        if(_allowPhantom)
        {
            soot.options.Options.v().set_allow_phantom_refs(true);
        }

        Collection<SootClass> classes = new ArrayList<SootClass>();
        for(String className : provider.getClassNames())
        {
            scene.loadClass(className, SootClass.SIGNATURES);
            SootClass c = scene.loadClass(className, SootClass.BODIES);

            if (isApplicationClass(c))
                c.setApplicationClass();

            classes.add(c);
        }

        /* For simulating the FileSystem class, we need the implementation
           of the FileSystem, but the classes are not loaded automatically
           due to the indirection via native code.
        */
        addCommonDynamicClass(scene, provider, "java.io.UnixFileSystem");
        addCommonDynamicClass(scene, provider, "java.io.WinNTFileSystem");
        addCommonDynamicClass(scene, provider, "java.io.Win32FileSystem");

        /* java.net.URL loads handlers dynamically */
        addCommonDynamicClass(scene, provider, "sun.net.www.protocol.file.Handler");
        addCommonDynamicClass(scene, provider, "sun.net.www.protocol.ftp.Handler");
        addCommonDynamicClass(scene, provider, "sun.net.www.protocol.http.Handler");
        addCommonDynamicClass(scene, provider, "sun.net.www.protocol.https.Handler");
        addCommonDynamicClass(scene, provider, "sun.net.www.protocol.jar.Handler");

        scene.loadNecessaryClasses();

        Database db;
        if(_trap)
            db = new TRAPDatabase(new File(_outputDir));
        else
            db = new CSVDatabase(new File(_outputDir));
        FactWriter writer = new FactWriter(db);
        FactGenerator generator = new FactGenerator(writer, _ssa);

        for(SootClass c : classes)
        {
            if (c.isApplicationClass())
                writer.writeApplicationClass(c);
        }

        if(_mode == Mode.FULL)
        {
            classes = scene.getClasses();
        }

        for(SootClass c : classes)
        {
            generator.generate(c);
        }

        db.close();
    }

    public static void addCommonDynamicClass(Scene scene, ClassProvider provider, String className)
    {
        if(provider.find(className) != null)
        {
            scene.addBasicClass(className);
        }

    }

    private static void handleDependence(String mainClass) {
        if (mainClass == null) {
            return;
        }
        // FindBugs
        if (mainClass.equals("edu.umd.cs.findbugs.FindBugs2")) {
            _inputs.add("jars/findbugs/coreplugin.jar");
            _libraries.addAll(Arrays.asList(
                    "jars/findbugs/asm-3.0.jar",
                    "jars/findbugs/asm-commons-3.0.jar",
                    "jars/findbugs/asm-tree-3.0.jar",
                    "jars/findbugs/bcel.jar",
                    "jars/findbugs/dom4j-full.jar"
            ));
        }
        // Sunflow
        if (mainClass.equals("SunflowGUI")) {
            _libraries.add("jars/sunflow/janino.jar");
        }
        // Batik
        if (mainClass.equals("org.apache.batik.apps.svgbrowser.Main")) {
            _libraries.addAll(Arrays.asList(
                    "jars/batik/1.6.1/batik-rasterizer.jar",
                    "jars/batik/1.6.1/batik-slideshow.jar",
                    "jars/batik/1.6.1/batik-svgpp.jar",
                    "jars/batik/1.6.1/batik-ttf2svg.jar",
                    "jars/batik/1.6.1/lib/batik-awt-util.jar",
                    "jars/batik/1.6.1/lib/batik-bridge.jar",
//                    "jars/batik/1.6.1/lib/batik-css.jar",
//                    "jars/batik/1.6.1/lib/batik-dom.jar",
                    "jars/batik/1.6.1/lib/batik-ext.jar",
                    "jars/batik/1.6.1/lib/batik-extension.jar",
                    "jars/batik/1.6.1/lib/batik-gui-util.jar",
                    "jars/batik/1.6.1/lib/batik-gvt.jar",
//                    "jars/batik/1.6.1/lib/batik-parser.jar",
                    "jars/batik/1.6.1/lib/batik-script.jar",
                    "jars/batik/1.6.1/lib/batik-svg-dom.jar",
                    "jars/batik/1.6.1/lib/batik-svggen.jar",
                    "jars/batik/1.6.1/lib/batik-swing.jar",
//                    "jars/batik/1.6.1/lib/batik-transcoder.jar",
                    "jars/batik/1.6.1/lib/batik-util.jar",
                    "jars/batik/1.6.1/lib/batik-xml.jar",
                    "jars/batik/1.6.1/lib/js.jar",
                    "jars/batik/1.6.1/lib/pdf-transcoder.jar",
                    "jars/batik/1.6.1/lib/xerces_2_5_0.jar",
                    "jars/batik/1.6.1/lib/xml-apis.jar"
            ));
        }

        // for DaCapo 2009
        if (inputContains("dacapo-2009")) {
            if (inputContains("avrora.jar")) {
                _libraries.add("jars/dacapo-2009/avrora-deps.jar");
            }
            if (inputContains("luindex.jar")) {
                _libraries.add("jars/dacapo-2009/luindex-deps.jar");
            }
            if (inputContains("lusearch.jar")) {
                _libraries.add("jars/dacapo-2009/lusearch-deps.jar");
            }
            if (inputContains("h2.jar")) {
                _libraries.add("jars/dacapo-2009/h2-deps.jar");
            }
            if (inputContains("pmd.jar")) {
                _libraries.add("jars/dacapo-2009/pmd-deps.jar");
            }
            if (inputContains("xalan.jar")) {
                _libraries.add("jars/dacapo-2009/xalan-deps.jar");
            }
            if (inputContains("batik.jar")) {
                _libraries.add("jars/dacapo-2009/batik-deps.jar");
            }
            if (inputContains("sunflow09.jar")) {
                _libraries.add("jars/dacapo-2009/sunflow-deps.jar");
            }
            if (inputContains("eclipse.jar")) {
                _libraries.add("jars/dacapo-2009/eclipse-deps.jar");
            }
            if (inputContains("eclipse-huge.jar")) {
                _libraries.add("jars/dacapo-2009/eclipse-deps.jar");
            }
        }
    }

    private static boolean inputContains(String name) {
        for (String input : _inputs) {
            if (input.contains(name)) {
                return true;
            }
        }
        return false;
    }

    private static void turnoffSootOutput() {
        // Turn off the output of Soot.
        System.setOut(new PrintStream(new OutputStream() {
            public void write(int b) {
                //DO NOTHING
            }
        }));
    }
}
