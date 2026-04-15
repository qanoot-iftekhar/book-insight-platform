import React, { useState, useEffect } from 'react';
import axios from 'axios';

const API = 'http://localhost:8000/api';

function App() {
  const [books, setBooks] = useState([]);
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchBooks();
  }, []);

  const fetchBooks = async () => {
    const res = await axios.get(`${API}/books/`);
    setBooks(res.data);
  };

  const askQuestion = async () => {
    setLoading(true);
    const res = await axios.post(`${API}/ask/`, { question });
    setAnswer(res.data);
    setLoading(false);
  };

  return (
    <div className="p-8 bg-gray-900 min-h-screen text-white">
      <h1 className="text-4xl font-bold mb-8">📚 Book Insights</h1>
      
      <div className="grid md:grid-cols-2 gap-8">
        {/* Book List */}
        <div className="bg-gray-800 p-6 rounded-xl">
          <h2 className="text-2xl font-bold mb-4">Books ({books.length})</h2>
          {books.map(book => (
            <div key={book.id} className="border-b border-gray-700 py-3">
              <h3 className="font-bold">{book.title}</h3>
              <p className="text-gray-400">{book.author} ⭐ {book.rating}</p>
            </div>
          ))}
        </div>

        {/* Q&A Section */}
        <div className="bg-gray-800 p-6 rounded-xl">
          <h2 className="text-2xl font-bold mb-4">Ask AI about books</h2>
          <textarea
            className="w-full p-3 rounded bg-gray-700 text-white mb-4"
            rows="3"
            placeholder="e.g., Suggest a good mystery book..."
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
          />
          <button
            className="bg-blue-600 px-6 py-2 rounded hover:bg-blue-700"
            onClick={askQuestion}
            disabled={loading}
          >
            {loading ? 'Thinking...' : 'Ask AI'}
          </button>
          
          {answer && (
            <div className="mt-6 p-4 bg-gray-700 rounded">
              <p className="font-bold mb-2">Answer:</p>
              <p>{answer.answer}</p>
              {answer.sources && (
                <p className="text-sm text-gray-400 mt-2">
                  Sources: {answer.sources.map(s => s.title).join(', ')}
                </p>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;