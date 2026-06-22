import { useState } from "react";

import MainLayout from "../layouts/MainLayout";

import { searchItems } from "../api/searchApi";

import { Folder, FileText } from "lucide-react";

function SearchPage() {
  const [query, setQuery] = useState("");

  const [results, setResults] = useState(null);

  const handleSearch = async () => {
    if (!query.trim()) return;

    const data = await searchItems(query);

    setResults(data);
  };

  return (
    <MainLayout>
      <h1 className="text-4xl font-bold mb-8">Search</h1>

      <div className="flex gap-3 mb-6">
        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search files or folders..."
          className="flex-1 bg-zinc-900 border border-zinc-800 rounded-lg px-4 py-3"
        />

        <button
          onClick={handleSearch}
          className="px-6 py-3 bg-white text-black rounded-lg font-semibold"
        >
          Search
        </button>
      </div>

      {results && (
        <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-6">
          <h2 className="text-xl font-bold mb-4">Files</h2>

          {results.files.length === 0 ? (
            <p className="text-zinc-500">No files found</p>
          ) : (
            results.files.map((file) => (
              <div key={file.id} className="py-2">
                <div className="flex items-center gap-3">
                  <FileText size={18} />
                  {file.name}
                </div>
              </div>
            ))
          )}

          <h2 className="text-xl font-bold mt-8 mb-4">Directories</h2>

          {results.directories.length === 0 ? (
            <p className="text-zinc-500">No folders found</p>
          ) : (
            results.directories.map((directory) => (
              <div key={directory.id} className="flex items-center gap-3 py-2">
                <Folder size={18} />
                {directory.name}
              </div>
            ))
          )}
        </div>
      )}
    </MainLayout>
  );
}

export default SearchPage;
