import decay from "https://esm.sh/gh/clux/decay";

Deno.serve(async (req) => {
  const { gravity, upVotes, created_at } = await req.json();

  // create the hackerhot factory
  var hackerHotScoreFactory = decay.hackerHot(gravity);

  // calc the score
  var currScore = hackerHotScoreFactory(upVotes, new Date(created_at));

  // return the array of scores to be updated
  const data = {
    score: currScore,
  };

  return new Response(
    JSON.stringify(data),
    { headers: { "Content-Type": "application/json" } },
  )
})
