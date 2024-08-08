export default function SongCard({song}){

    return(
        <div>
            <h3>{song.title}</h3>
            <p>{song.artist}</p>
            <a href={song.youtube_link} target="_blank">Link to video</a>
            {/* <iframe width="560" height="315" src={song.youtube_link} title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe> */}
        </div>
    )
}