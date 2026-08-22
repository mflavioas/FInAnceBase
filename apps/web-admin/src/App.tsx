import { useState, useEffect } from 'react';
import { Database, UploadCloud, Activity, Settings, Plus, LayoutDashboard, Globe, FileText, CheckCircle2, AlertCircle } from 'lucide-react';

interface Source {
  id: string;
  name: string;
  url: string;
  source_type: string;
  status: string;
}

function App() {
  const [sources, setSources] = useState<Source[]>([]);
  const [isAdding, setIsAdding] = useState(false);
  const [toast, setToast] = useState<{ message: string; type: 'success' | 'error' } | null>(null);
  
  const [formData, setFormData] = useState({
    name: '',
    url: '',
    source_type: 'BACEN'
  });
  
  const [file, setFile] = useState<File | null>(null);

  const showToast = (message: string, type: 'success' | 'error') => {
    setToast({ message, type });
    setTimeout(() => setToast(null), 4000);
  };

  const fetchSources = async () => {
    try {
      const res = await fetch('http://localhost:8000/sources/');
      if (res.ok) {
        const data = await res.json();
        setSources(data);
      }
    } catch (e) {
      console.error("Erro ao buscar fontes:", e);
    }
  };

  useEffect(() => {
    fetchSources();
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const isFileUpload = formData.source_type === 'INTERNAL' || formData.source_type === 'MANUAL';
    
    try {
      let res;
      if (isFileUpload) {
        if (!file) {
          showToast("Por favor, selecione um arquivo para anexar.", "error");
          return;
        }
        const data = new FormData();
        data.append('name', formData.name);
        data.append('file', file);
        
        res = await fetch('http://localhost:8000/sources/upload', {
          method: 'POST',
          body: data
        });
      } else {
        if (!formData.url) {
          showToast("A URL não pode estar vazia.", "error");
          return;
        }
        res = await fetch('http://localhost:8000/sources/', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            name: formData.name,
            url: formData.url,
            source_type: formData.source_type
          })
        });
      }

      if (res.ok) {
        setFormData({ name: '', url: '', source_type: 'BACEN' });
        setFile(null);
        setIsAdding(false);
        showToast("Fonte cadastrada com sucesso!", "success");
        fetchSources();
      } else {
        showToast("Erro da API ao tentar cadastrar fonte. Tente novamente.", "error");
      }
    } catch (e) {
      showToast("Erro de conexão. A API está rodando?", "error");
    }
  };

  return (
    <div className="admin-container">
      {toast && (
        <div className={`toast ${toast.type}`}>
          {toast.type === 'success' ? <CheckCircle2 size={20} /> : <AlertCircle size={20} />}
          <span>{toast.message}</span>
        </div>
      )}

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
                  <input required type="text" value={formData.name} onChange={e => setFormData({...formData, name: e.target.value})} placeholder="Ex: Normativa BACEN 2024 ou Contrato Interno" />
                </div>
                
                <div className="form-group">
                  <label>Tipo (Categoria)</label>
                  <select value={formData.source_type} onChange={e => setFormData({...formData, source_type: e.target.value})}>
                    <option value="BACEN">Externa - BACEN (URL)</option>
                    <option value="CMN">Externa - CMN (URL)</option>
                    <option value="PLANALTO">Externa - Planalto (URL)</option>
                    <option value="API">Externa - Integração de API (URL)</option>
                    <option value="INTERNAL">Interno - Upload de Documento (PDF/Word)</option>
                    <option value="MANUAL">Manual - Base Legada Local</option>
                  </select>
                  <small className="help-text">
                    Tipos externos requerem uma URL válida. Tipos internos exigem o upload do arquivo.
                  </small>
                </div>

                {(formData.source_type === 'INTERNAL' || formData.source_type === 'MANUAL') ? (
                  <div className="form-group">
                    <label>Anexar Arquivo</label>
                    <input type="file" onChange={e => setFile(e.target.files ? e.target.files[0] : null)} className="file-input" />
                  </div>
                ) : (
                  <div className="form-group">
                    <label>URL / Caminho</label>
                    <input type="text" value={formData.url} onChange={e => setFormData({...formData, url: e.target.value})} placeholder="https://..." />
                  </div>
                )}
                
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
                    <th>URL ou Arquivo</th>
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
