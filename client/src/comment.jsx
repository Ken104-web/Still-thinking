import  { useState  } from "react";

function CommentSection({ reviewId }){
    const [newcomments, setNewComments] = useState("");

    const handleCommentSubmit = () => {
        
        setNewComments("");
    };
    return (
        <div id="comment">
        <textarea
          rows="3"
          cols="30"
          value={newcomments}
          onChange={(e) => setNewComments(e.target.value)}
        />
        <button onClick={handleCommentSubmit}>Submit Comment</button>
      </div>
    );
}

export default CommentSection;