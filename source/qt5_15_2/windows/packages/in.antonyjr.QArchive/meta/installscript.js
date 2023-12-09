function Component() {
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
    }
}

Component.prototype.isDefault = function()
{
    return true;
}
