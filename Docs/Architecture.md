+------------------+
         |    User / UI     |
         +--------+---------+
                  |
                  v
         +------------------+
         |  Orchestrator    | < Supervisor loop, traces
         +---+---+---+---+--+
             |   |   |   |
 Planner --> Research Writer Scheduler
  (Gemini)   (Search) (Gemini) (Calendar)
             |       |
         Memory <----|
         (FAISS)      \
                       Verifier (Gemini)
                       /  |   \
                  Approve Edit Deny
