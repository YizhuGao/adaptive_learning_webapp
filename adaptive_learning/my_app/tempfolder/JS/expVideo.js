document.querySelectorAll('.video-tile').forEach(tile => {
    // Add the play icon dynamically (if not already in HTML)
    if (!tile.querySelector('.play-icon')) {
        const playIcon = document.createElement('div');
        playIcon.classList.add('play-icon');
        tile.appendChild(playIcon);
    }

    // Use event delegation on tile (or play icon) to open modal
    tile.addEventListener('click', function (event) {
        event.preventDefault();

        // Ignore if click is on close button or modal itself
        if (event.target.classList.contains('close-button')) return;

        // Find iframe inside the clicked tile
        const iframe = tile.querySelector('iframe.video-frame');
        if (!iframe) return;

        const videoUrl = iframe.getAttribute('src');

        const modal = document.getElementById('videoModal');
        const modalIframe = document.getElementById('modalVideoFrame');

        modalIframe.setAttribute('src', videoUrl);
        modal.style.display = 'flex';  // use flex to center content
    });
});

// Close modal on close button click
document.querySelector('.close-button').addEventListener('click', () => {
    const modal = document.getElementById('videoModal');
    const modalIframe = document.getElementById('modalVideoFrame');

    modalIframe.setAttribute('src', '');  // stop video
    modal.style.display = 'none';
});

// ✅ Close modal when clicking outside modal content
window.addEventListener('click', (event) => {
    const modal = document.getElementById('videoModal');
    const modalContent = document.querySelector('.modal-content');

    if (event.target === modal) {
        const modalIframe = document.getElementById('modalVideoFrame');
        modalIframe.setAttribute('src', ''); // stop video
        modal.style.display = 'none';       // close modal
    }
});
