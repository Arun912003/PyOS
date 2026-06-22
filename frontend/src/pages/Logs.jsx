import { useEffect, useState } from "react";

import MainLayout from "../layouts/MainLayout";

import { getLogs } from "../api/logsApi";

function Logs() {

  const [logs, setLogs] =
    useState([]);

  useEffect(() => {
    fetchLogs();
  }, []);

  const fetchLogs = async () => {

    const data =
      await getLogs();

    setLogs(data);
  };

  return (
    <MainLayout>

      <h1 className="text-4xl font-bold mb-8">
        Activity Logs
      </h1>

      <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-6">

        {logs.length === 0 ? (

          <p className="text-zinc-500">
            No logs found
          </p>

        ) : (

          logs.map((log) => (

            <div
              key={log.id}
              className="border-b border-zinc-800 py-3"
            >

              <p className="font-medium">
                {log.action}
              </p>

              <p className="text-sm text-zinc-500">
                {log.created_at}
              </p>

            </div>

          ))
        )}

      </div>

    </MainLayout>
  );
}

export default Logs;