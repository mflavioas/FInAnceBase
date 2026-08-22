import { useState, useEffect } from 'react';
import { Database, UploadCloud, Activity, Settings, Plus, LayoutDashboard, Globe, FileText, CheckCircle2 } from 'lucide-react';

interface Source {
  id: string;
  name: string;
  url: string;
  source_type: 'WEB' | 'DOCUMENT' | 'DATABASE';
  status: 'ACTIVE' | 'PROCESSING' | 'ERROR';
}

function App() {
  const [sources, setSources] = useState<Source[]>([]);
  const [isAdding, setIsAdding] = useState(false);
  
  const [formData, setFormData] = useState({
    name: '',
    url: '',
    source_type: 'WEB'
  });

  const fetchSources = async () => {
    try {
      const res = await fetch('http://localhost:8000/sources/');
      const data = await res.json();
      setSources(data);
    } catch (e) {
      console.error("Erro ao buscar fontes:", e);
    }
  };

  useEffect(() => {
    fetchSources();
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const res = await fetch('http://localhost:8000/sources/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
      });
      if (res.ok) {
        setFormData({ name: '', url: '', source_type: 'WEB' });
        setIsAdding(false);
        fetchSources();
      }
    } catch (e) {
      console.error("Erro ao adicionar fonte:", e);
    }
  };

  return (
    <div className="admin-container">
      <aside className="sidebar">
        <div className="logo">
          <Database className="logo-icon" size={24} />
          <span>FinKnowledge</span>
        </div>
        <nav>
          <a href="#" className="nav-item active">
            <LayoutDashboard size={20} /> Dashboard
          </a>
          <a href="#" className="nav-item">
            <Globe size={20} /> Fontes de Dados
          </a>
          <a href="#" className="nav-item">
            <FileText size={20} /> Revisão de Docs
          </a>
          <a href="#" className="nav-item">
            <Activity size={20} /> Monitoramento
          </a>
          <a href="#" className="nav-item mt-auto">
            <Settings size={20} /> Configurações
          </a>
        </nav>
      </aside>

      <main className="main-content">
        <header className="topbar">
          <h2>Dashboard Administrativo</h2>
          <div className="user-profile">Admin</div>
        </header>

        <div className="content-wrapper">
          <div className="header-actions">
            <div>
              <h3>Gestão de Conhecimento</h3>
              <p>Adicione links e integrações para os Agentes indexarem.</p>
            </div>
            <button className="btn-primary" onClick={() => setIsAdding(!isAdding)}>
              <Plus size={18} /> Adicionar Fonte
            </button>
          </div>

          {isAdding && (
            <div className="card add-card">
              <h4>Nova Fonte de Dados</h4>
              <form onSubmit={handleSubmit} className="add-form">
                <div className="form-group">
                  <label>Nome do Contexto</label>
                  <input required type="text" value={formData.name} onChange={e => setFormData({...formData, name: e.target.value})} placeholder="Ex: Normativa Bacen 2024" />
                </div>
                <div className="form-group">
                  <label>URL ou Caminho</label>
                  <input required type="text" value={formData.url} onChange={e => setFormData({...formData, url: e.target.value})} placeholder="https://..." />
                </div>
                <div className="form-group">
                  <label>Tipo</label>
                  <select value={formData.source_type} onChange={e => setFormData({...formData, source_type: e.target.value})}>
                    <option value="WEB">Site / Web</option>
                    <option value="DOCUMENT">Documento (PDF/Docx)</option>
                    <option value="DATABASE">Banco de Dados</option>
                  </select>
                </div>
                <div className="form-actions">
                  <button type="button" className="btn-text" onClick={() => setIsAdding(false)}>Cancelar</button>
                  <button type="submit" className="btn-primary"><UploadCloud size={18} /> Ingestar Dados</button>
                </div>
              </form>
            </div>
          )}

          <div className="card table-card">
            <h4>Fontes Indexadas</h4>
            {sources.length === 0 ? (
              <div className="empty-state">
                <p>Nenhuma fonte de dados indexada ainda.</p>
              </div>
            ) : (
              <table className="data-table">
                <thead>
                  <tr>
                    <th>Nome</th>
                    <th>Tipo</th>
                    <th>URL</th>
                    <th>Status</th>
                  </tr>
                </thead>
                <tbody>
                  {sources.map(source => (
                    <tr key={source.id}>
                      <td>{source.name}</td>
                      <td>
                        <span className="badge type">{source.source_type}</span>
                      </td>
                      <td className="url-col">{source.url}</td>
                      <td>
                        <span className="badge status active">
                          <CheckCircle2 size={14} /> {source.status}
                        </span>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            )}
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
