import { useEffect, useState } from "react";

import MainLayout from "../layouts/MainLayout";

import { getHistory }
from "../api/historyApi";

function History() {

  const [history, setHistory] =
    useState([]);

  useEffect(() => {
    fetchHistory();
  }, []);

  const fetchHistory =
    async () => {

      const data =
        await getHistory();

      setHistory(data);
    };

  return (
    <MainLayout>

      <h1 className="text-4xl font-bold mb-8">
        Command History
      </h1>

      <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-6">

        {history.length === 0 ? (

          <p className="text-zinc-500">
            No history found
          </p>

        ) : (

          history.map((item) => (

            <div
              key={item.id}
              className="border-b border-zinc-800 py-3"
            >

              <p className="font-medium">
                {item.command}
              </p>

              <p className="text-sm text-zinc-500">
                {item.created_at}
              </p>

            </div>

          ))
        )}

      </div>

    </MainLayout>
  );
}

export default History;