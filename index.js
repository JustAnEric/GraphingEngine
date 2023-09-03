document.querySelector('html').addEventListener('pointerup', function(event) {
    // Call navigator.bluetooth.requestDevice
    navigator.bluetooth.requestDevice()
});