// audioRecorder.js

function setupAudioRecorder(startButtonId, stopButtonId, audioPlayerId, playButtonId) {
  let mediaRecorder;
  let recordedChunks = [];
  var playable = false;

  const startRecordingButton = document.getElementById(startButtonId);
  const stopRecordingButton = document.getElementById(stopButtonId);

  // if playRecordingButton, audioPlayerId are provided
  if (audioPlayerId && playButtonId) {
    const playRecordingButton = document.getElementById(playButtonId);
    var audioPlayer = document.getElementById(audioPlayerId);
    playable = true;
    playRecordingButton.addEventListener('click', playRecording);
  }


  startRecordingButton.addEventListener('click', startRecording);
  stopRecordingButton.addEventListener('click', stopRecording);


  async function startRecording() {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });

    mediaRecorder = new MediaRecorder(stream);

    mediaRecorder.ondataavailable = (event) => {
      if (event.data.size > 0) {
        recordedChunks.push(event.data);
      }
    };

    mediaRecorder.onstop = () => {
      const audioBlob = new Blob(recordedChunks, { type: 'audio/wav' });
      const audioUrl = URL.createObjectURL(audioBlob);
      if(playable){
        audioPlayer.src = audioUrl;
        playRecordingButton.disabled = false;
      }


      // Convert audio blob to Base64 string
      const reader = new FileReader();
      reader.onloadend = function () {
        const base64Data = reader.result.split(',')[1];
        // Trigger a custom event with the Base64-encoded audio data
        document.dispatchEvent(new CustomEvent('audioRecorded', { detail: base64Data }));
      };
      reader.readAsDataURL(audioBlob);
    };

    mediaRecorder.start();
    startRecordingButton.style.display = 'none';
    stopRecordingButton.style.display = 'block';

    // replace class Rec with noRec to startRecordingButton
    startRecordingButton.classList.remove('noRec');
    startRecordingButton.classList.add('Rec');
  }

  function stopRecording() {
    if (mediaRecorder.state !== 'inactive') {
      mediaRecorder.stop();

      startRecordingButton.style.display = 'block';
      stopRecordingButton.style.display = 'none';

      // replace class Rec with noRec to startRecordingButton
      startRecordingButton.classList.remove('Rec');
      startRecordingButton.classList.add('noRec');
    }
  }

  function playRecording() {
    audioPlayer.play();
  }
}
