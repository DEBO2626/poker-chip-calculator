@echo off
set JAVA_HOME=C:\Users\john_\.bubblewrap\jdk\jdk-17.0.11+9
set ANDROID_HOME=C:\Users\john_\AppData\Local\Android\Sdk
echo JAVA_HOME=%JAVA_HOME%
echo ANDROID_HOME=%ANDROID_HOME%
call gradlew.bat bundleRelease
