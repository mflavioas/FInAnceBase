import { useState, useRef, useEffect } from 'react';
import { Send, Bot, User, Loader2 } from 'lucide-react';

interface Message {
  id: string;
  text: string;
  sender: 'user' | 'bot';
}

function App() {
  const [messages, setMessages] = useState<Message[]>([
    { id: '1', text: 'Olá! Sou o Orquestrador do FinKnowledge. Como posso ajudar você hoje?', sender: 'bot' }
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };
  
  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || isLoading) return;

    const userMessage: Message = { id: Date.now().toString(), text: input, sender: 'user' };
    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setIsLoading(true);

    try {
      const response = await fetch('http://localhost:8000/assistant/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          query: userMessage.text,
          session_id: 'chat-ui-session-1'
        }),
      });
      
      const data = await response.json();
      
      const botMessage: Message = {
        id: (Date.now() + 1).toString(),
        text: data.response || 'Desculpe, não consegui obter uma resposta.',
        sender: 'bot'
      };
      setMessages(prev => [...prev, botMessage]);
    } catch (error) {
      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        text: 'Erro ao conectar com a API. Verifique se o backend está rodando.',
        sender: 'bot'
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="chat-container">
      <header className="chat-header">
        <Bot size={28} className="header-icon" />
        <div>
          <h1>FinKnowledge Chat</h1>
          <p>Plataforma de Conhecimento Financeiro</p>
        </div>
      </header>

      <div className="messages-area">
        {messages.map((msg) => (
          <div key={msg.id} className={`message-wrapper ${msg.sender}`}>
            <div className="message-bubble">
              <div className="message-icon">
                {msg.sender === 'bot' ? <Bot size={20} /> : <User size={20} />}
              </div>
              <div className="message-content">
                {msg.text}
              </div>
            </div>
          </div>
        ))}
        {isLoading && (
          <div className="message-wrapper bot">
            <div className="message-bubble loading-bubble">
              <Loader2 className="spinner" size={20} />
              <span>Orquestrando agentes...</span>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <form className="input-area" onSubmit={handleSubmit}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Faça uma pergunta aos agentes..."
          disabled={isLoading}
        />
        <button type="submit" disabled={!input.trim() || isLoading}>
          <Send size={20} />
        </button>
      </form>
    </div>
  );
}

export default App;
