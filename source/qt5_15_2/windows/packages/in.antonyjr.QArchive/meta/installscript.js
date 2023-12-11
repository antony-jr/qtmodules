function Component() {
    var path = installer.value("InstallerDirPath");

    if (installer.fileExists("5.15.2")) {
        path = path + "/5.15.2";
    } else if(installer.fileExists("5.15.3")) {
        path = path + "/5.15.3";   
    } else if(installer.fileExists("5.15.4")) {
        path = path + "/5.15.4";    
    } else if(installer.fileExists("5.15.5")) {
        path = path + "/5.15.5";    
    } else if(installer.fileExists("5.15.6")) {
        path = path + "/5.15.6";    
    } else if(installer.fileExists("5.15.7")) {
        path = path + "/5.15.7";    
    } else if(installer.fileExists("5.15.8")) {
        path = path + "/5.15.8";    
    } else if(installer.fileExists("5.15.9")) {
        path = path + "/5.15.9";    
    } else if(installer.fileExists("5.15.10")) {
        path = path + "/5.15.10";    
    } else if(installer.fileExists("5.15.11")) {
        path = path + "/5.15.11";    
    } else if(installer.fileExists("5.15.12")) {
        path = path + "/5.15.12";    
    } else if(installer.fileExists("5.15.13")) {
        path = path + "/5.15.13";    
    } else if(installer.fileExists("5.15.14")) {
        path = path + "/5.15.14";    
    } else if(installer.fileExists("5.15.15")) {
        path = path + "/5.15.15";    
    } else if(installer.fileExists("5.15.16")) {
        path = path + "/5.15.16";    
    } else {
        path = path + "/QArchive";
    }

    installer.setValue("QtInstallDir", path)
    console.log("Path: " + path);

    /*
    if ( systemInfo.currentCpuArchitecture === "i386") {
        installer.componentByName("in.antonyjr.QArchive.windows.x86.msvc2015").setValue("Virtual", "false");
        installer.componentByName("in.antonyjr.QArchive.windows.x86.msvc2015").setValue("Default", "true");
    }*/

    if ( systemInfo.currentCpuArchitecture === "x86_64") {
        installer.componentByName("in.antonyjr.QArchive.windows.x64.msvc2019").setValue("Virtual", "false");
        installer.componentByName("in.antonyjr.QArchive.windows.x64.msvc2015").setValue("Virtual", "false"); 
        
        installer.componentByName("in.antonyjr.QArchive.windows.x64.msvc2019").setValue("Default", "true");

        installer.componentByName("in.antonyjr.QArchive").setValue("TargetDir", path);
        installer.componentByName("in.antonyjr.QArchive.windows.x64.msvc2019").setValue("TargetDir", path);
        installer.componentByName("in.antonyjr.libarchive.windows.x64.msvc2019").setValue("TargetDir", path);
        installer.componentByName("in.antonyjr.QArchive.windows.x64.msvc2015").setValue("TargetDir", path);
        installer.componentByName("in.antonyjr.libarchive.windows.x64.msvc2015").setValue("TargetDir", path);
   
    }
}

Component.prototype.isDefault = function()
{
    return true;
}
