const fetchVideo = async (session_id, video_id) => {
    const req = await fetch(`http://localhost:5001/videos/${session_id}/${video_id}`)
    const data = await req.json();
    const videos = req.status === 200 ? data.videos : [];
    return videos;
  }

export default fetchVideo;