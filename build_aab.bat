@echo off
cd /d "c:\Users\john_\Desktop\Poker chip"
set JAVA_HOME=C:\Users\john_\.bubblewrap\jdk\jdk-17.0.11+9
set ANDROID_HOME=C:\Users\john_\AppData\Local\Android\Sdk
echo Starting build...
call gradlew.bat bundleRelease
echo Build exit code: %ERRORLEVEL%
