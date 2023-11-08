import decay from "https://esm.sh/gh/clux/decay";

Deno.serve(async (req) => {
  const { gravity, data_rows } = await req.json();

  // create the hackerhot factory
  var hackerHotScoreFactory = decay.hackerHot(gravity);

  var scoresDict = {};

  data_rows.forEach((row) => {
    // calc the score for this row
    var currScore = hackerHotScoreFactory(row['upvotes'], new Date(row['created_at']));
    // store the id of the current row with it's hackerhot score
    scoresDict[row['id']] = currScore;
  });

  // return the array of scores to be updated
  const data = {
    scores: scoresDict,
  };

  return new Response(
    JSON.stringify(data),
    { headers: { "Content-Type": "application/json" } },
  )
})
