+++
title = "Gaming"
showMetadata = false
+++

Add me on your favorite gaming network:

* [BattleTag](https://us.battle.net) / Linuturk#1600
* [Bethesda](https://bethesda.net/en/) / Linuturk
* [Discord](https://discordapp.com) / Linuturk#9335
* [EA/Origin](https://myaccount.ea.com) / Linuturk
* [Epic Games](https://www.epicgames.com) / Linuturk
* [Nintendo](https://my.nintendo.com/) / Linuturk 0990-0190-4533
* [Playstation Network](https://my.playstation.com/Linuturk) / Linuturk
* [Steam](https://steamcommunity.com/id/linuturk) / linuturk
* [Twitch](https://www.twitch.tv/linuturk) / linuturk
* [Warframe](https://www.warframe.com/) / Linuturk
* [Xbox Live](https://www.xbox.com/) / Linuturk

## Extra Life

<div style="max-width: 340px; padding: 1.25rem; border-radius: 10px; background: #2d1b4e; color: #fff; border-top: 6px solid #e5007d;">
  <div style="font-weight: 700; font-size: 1.1rem;">Play games. Heal kids.</div>
  <div style="font-size: .9rem; margin: .25rem 0 1rem; opacity: .85;">I play games to raise money for children's hospitals through Extra Life.</div>
  <div style="background: rgba(255,255,255,.2); border-radius: 999px; height: 18px; overflow: hidden;">
    <div id="el-fill" style="background: linear-gradient(90deg, #e5007d, #ff6a3d); height: 100%; width: 0; border-radius: 999px; transition: width .5s;"></div>
  </div>
  <div id="el-status" style="font-size: .95rem; font-weight: 600; margin: .5rem 0 1rem;">Loading…</div>
  <a href="https://dd.extra-life.org/participants/linuturk/donate" style="display: inline-block; padding: .5rem 1.25rem; border-radius: 999px; background: #e5007d; color: #fff; font-weight: 700; text-decoration: none;">Donate</a>
</div>
<script>
// Update the participant ID each year.
fetch("https://dd.extra-life.org/api/participants/581170")
  .then(function (r) { if (!r.ok) throw new Error("HTTP " + r.status); return r.json(); })
  .then(function (d) {
    var pct = Math.min(100, d.sumDonations / d.fundraisingGoal * 100);
    document.getElementById("el-fill").style.width = pct + "%";
    document.getElementById("el-status").textContent =
      "$" + d.sumDonations + " raised of $" + d.fundraisingGoal + " goal";
  })
  .catch(function () {
    document.getElementById("el-status").textContent = "";
  });
</script>
