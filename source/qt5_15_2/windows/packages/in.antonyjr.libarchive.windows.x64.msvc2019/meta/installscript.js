function Component() {

}

Component.prototype.createOperationsForArchive = function(archive)
{
    // don't use the default operation
    // component.createOperationsForArchive(archive);

    // add an extract operation with a modified path
    console.log("LibArchive InstallDir: " + installer.value("QtInstallDir"));
    component.addOperation("Extract", archive, installer.value("QtInstallDir"));
}

Component.prototype.isDefault = function()
{
    return true;
}
