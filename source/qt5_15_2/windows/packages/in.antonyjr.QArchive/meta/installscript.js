function Component() {
    //var qtVersion = qtversion();

    // Log the Qt version to the installer log
    //installer.setValue("QtVersion", qtVersion);
    //console.log("Qt version: " + qtVersion);
    var path = installer.value("InstallerDirPath");

    if (installer.fileExists("5.15.2")) {
        path = path + "\\5.15.2";
    } else {
        path = path + "\\QArchive";
    }

    console.log("Path: " + path);

    /*
    if ( systemInfo.currentCpuArchitecture === "i386") {
        installer.componentByName("in.antonyjr.QArchive.windows.x86.msvc2019").setValue("Virtual", "false");
        installer.componentByName("in.antonyjr.QArchive.windows.x86.msvc2019").setValue("Default", "true");
    }
    */

    if ( systemInfo.currentCpuArchitecture === "x86_64") {
        installer.componentByName("in.antonyjr.QArchive.windows.x64.msvc2019").setValue("Virtual", "false");
        //installer.componentByName("in.antonyjr.QArchive.windows.x64.msvc2015").setValue("Virtual", "false"); 
        installer.componentByName("in.antonyjr.QArchive.windows.x64.msvc2019").setValue("Default", "true");

        installer.componentByName("in.antonyjr.QArchive").setValue("TargetDir", path);
        installer.componentByName("in.antonyjr.QArchive.windows.x64.msvc2019").setValue("TargetDir", path);
        installer.componentByName("in.antonyjr.libarchive.windows.x64.msvc2019").setValue("TargetDir", path);
    }
}

Component.prototype.isDefault = function()
{
    return true;
}
