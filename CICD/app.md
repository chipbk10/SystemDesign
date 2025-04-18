- **write code** by using a specific language: java, python, etc.
- **compile code** refers to translating source code into machine code, performed by a compiler (javac for java, gcc for C++). For interpreted languages (e.g., Python, Javascript), there is no compilation.
- **build code** refers to preparing the code for execution or distribution. It may involve:
  - compile code
  - bundle assets, **minify** code (eliminate unused code or resources), **obfuscate** code (shorten the name of classes & members to reduce the file size)
  - resolve dependencies
  - link object files with library
  - packaging the app refers to make the app portable, self-contained, or ready for its target platform
- **runtime** refers to the software environment or components required to execute an application (e.g., JRE for java, Python Interpreter, Browser for web code). If you distribute the app, ensure the target machine has these components.
- **test code** refers to run the code locally to ensure it works as expected
- **deploy code** refers to make your app available for use in its intended environment (e.g., a server, user's device, or cloud platform). It involves:
  - **packaging**: preparing the app for distribution (e.g., `.apk` for Android, a docker container for server)
  - **transferring**: move the app to the target environment (e.g., uploading a docker container to a web server, publishing `.apk` to app store, or install `.exe` file on a user's PC)
  - **configuring**: set up the environment to run the app (e.g., installing dependencies, configuring a database, or setting environment variables)
  - **running**: start the app in production (e.g., lauching a web server `node server.js`)
- **monitor**: monitor the app for errors or performance issue (e.g., using logs or analytics tools)
- **maintain**: update the app to fix bugs or add features, which may involve repeating steps (write, build, test, deploy)
  
