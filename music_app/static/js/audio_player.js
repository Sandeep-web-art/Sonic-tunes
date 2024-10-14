document.addEventListener('DOMContentLoaded', function() {
    let allAudios = document.querySelectorAll('audio');

    function playOneAudio(audioToPlay) {
        allAudios.forEach(audio => {
            
            if (audio !== audioToPlay) {
                audio.pause();
                audio.currentTime = 0; 
            }
        });
        audioToPlay.play(); // Play the selected audio
    }

    allAudios.forEach(audio => {
        audio.addEventListener('play', () => {
            playOneAudio(audio); // Call the function when the audio plays
        });
    });
});