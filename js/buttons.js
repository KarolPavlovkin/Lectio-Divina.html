//**buttons.js**//

<script>
    const audio = document.getElementById('my-audio');
    const nextButton = document.getElementById('next-btn');

    // Autoplay & touch interaction logic
    function tryPlay() {
        audio.play().then(() => {
            document.removeEventListener('click', tryPlay);
            document.removeEventListener('touchstart', tryPlay);
        }).catch(error => {
            console.log("Autoplay blocked. Waiting for user tap.");
        });
    }

    window.addEventListener('DOMContentLoaded', tryPlay);
    document.addEventListener('click', tryPlay);
    document.addEventListener('touchstart', tryPlay);

    // Auto-advance when audio finishes
    audio.addEventListener('ended', function() {
        if (nextButton) nextButton.click();
    });

    // -------------------------------------------------------------
    // DOUBLE PRESS HARDWARE BUTTON LISTENER
    // -------------------------------------------------------------
    let lastVolUpTime = 0;
    let lastVolDownTime = 0;
    const DOUBLE_PRESS_DELAY = 400; // Time window in milliseconds (0.4 seconds)

    document.addEventListener('keydown', function(event) {
        const key = event.key || event.code;
        const now = Date.now();

        // 1. VOLUME UP DOUBLE-PRESS -> Trigger Next Button
        if (key === 'AudioVolumeUp' || key === 'VolumeUp') {
            event.preventDefault(); // Prevents system volume bar from showing
            
            if (now - lastVolUpTime < DOUBLE_PRESS_DELAY) {
                // Double press detected!
                if (nextButton) {
                    nextButton.click();
                }
                lastVolUpTime = 0; // Reset timer
            } else {
                lastVolUpTime = now;
            }
        }

        // 2. VOLUME DOWN DOUBLE-PRESS -> Toggle Play/Pause
        if (key === 'AudioVolumeDown' || key === 'VolumeDown') {
            event.preventDefault(); // Prevents system volume bar from showing
            
            if (now - lastVolDownTime < DOUBLE_PRESS_DELAY) {
                // Double press detected!
                if (audio) {
                    if (audio.paused) {
                        audio.play();
                    } else {
                        audio.pause();
                    }
                }
                lastVolDownTime = 0; // Reset timer
            } else {
                lastVolDownTime = now;
            }
        }
    });
</script>
