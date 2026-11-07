# Content log

## 2026-10-15 (manual session)
- 15 Oct 1300 carousel: 15 taareekh salary report (posts on the actual 15th)
- 15 Oct 2030 reel: Diwali gift = soan papdi
- 16 Oct 1300 reel: Friday 5:58 PM quick call
- 16 Oct 2030 carousel: Diwali safai 5 stages (23 days before Diwali, 8 Nov)
- 17 Oct 1300 image: Saturday plan (weakest, familiar joke)
- 17 Oct 2030 reel: India vs WI 5th T20I vs Mummy's almari (result-agnostic)

## 2026-10-15 00:22 IST (cloud run)
- Nothing missing: 15-17 Oct all 6 slots already queued (1 reel + 1 image/carousel per day). No new posts made.

## 2026-10-15 ~09:15 IST (cloud run, morning fill)
- New mix needs 2 reels/day; 15-17 Oct had only 1 reel each. Added a 1730 reel per day (3h+ from 1300/2030). Stories already full. No swaps.
- 15 Oct 1730 reel `sale-cart`: festive sale cart (14 items, Rs 38,499) vs balance Rs 1,240, Hera Pheri trio shock still, punch "1 phone cover, save for later". Trend: Flipkart BBD live since 9 Oct (verified), wording kept generic ("festive sale"). Shares: everyone has that cart, pairs with the 15 taareekh carousel.
- 16 Oct 1730 reel `papa-phone`: Papa's "phone mein kuch ho gaya" -> storage full, 3,000 good morning photos -> This Is Fine -> "kuch delete toh nahi kiya na?". Evergreen, tag-the-family-IT-guy share.
- 17 Oct 1730 reel `raat-2-baje`: 2:47 AM overthinking a 2014 "you too" to teacher, Jethalal thinking 4-panel, punch 5:10 AM / alarm 7. Evergreen.
- Risk: low. Analytics still too small (3 posts, 2 followers) to steer. Note: on-screen text can't render emoji (shows tofu), keep emoji in captions only.
- Script: content/scripts/reels1730_2026-10-15.py

## 2026-10-15 ~16:05 IST (cloud run, trend check)
- Nothing missing (15-17 Oct full, 18 Oct is beyond the 3-day cap). Trend check: X India led by #APJAbdulKalam (real person, skip), #Jailer2 (film/actor, off-niche), rest sensitive news. Sale/Diwali/IND vs WI 5th T20I (17 Oct, Bengaluru) already covered. No swap.

## 2026-10-15 22:15 IST (manual fix)
- Nothing published all day: Cloudinary secret had stray characters (fixed) + GitHub ran the schedule only 2x.
- Published from PC: 2030 diwali-gift reel, 2130 question story.
- Moved to backlog: 15-taareekh carousel (reuse on 15 Nov), sale-cart reel. Skipped (stale): 1000 mood story, 1330 teaser story.

## 2026-10-16 ~09:20 IST (cloud run, morning fill)
- 16-17 Oct already full. Filled Sun 18 Oct (2 days out, so evergreen only), new slot plan:
  - 1000 mood story: "Sunday hai" subah aaram / shaam Monday ka dar.
  - 1300 reel `sunday-dar`: Sunday 11 AM full aaram -> 6 PM pending mail yaad -> Hera Pheri dhak-dhak still -> Monday boss "weekend kaisa tha?". Shares: universal Sunday-scaries, tag-a-colleague.
  - 1330 teaser story of the 1300 reel.
  - 1730 image `sunday-relatives`: Welcome sofa template, relatives' salary/shaadi/mota audit, punch "Diwali pe phir aayenge beta". Shares: Diwali-season relatives dread, family group sends.
  - 2100 reel `salary-plan`: Gru's plan (salary aayi, SIP shuru, 4 din baad, balance Rs 212), punch "next month se pakka" (14 mahine se). Shares: tag the friend who's "starting SIP" for 2 years.
  - 2130 question story: Monday ke liye kitne alarm?
- Trend check: IND vs WI 5th T20I confirmed Sat 17 Oct 7 PM Bengaluru (already covered by 17 Oct 2030 reel). Festive sales still on, no end dates published. Nothing fresh and stronger, so no swap.
- Risk: low. Analytics still tiny (2 followers, Diwali gift reel 74 views, 0 shares). Script: content/scripts/batch_2026-10-16.py

## 2026-10-16 ~16:05 IST (cloud run, trend check)
- Nothing missing (16-18 Oct full, 19 Oct beyond 3-day cap). Trend check: today's news is a Mumbai infant tragedy, an actor's legal notice, a firecracker-ban court ruling and Reliance vs Musk over Starlink (all hard-limit or off-niche). IND vs WI 5th T20I confirmed Sat 17 Oct 7 PM Bengaluru, already covered by the 17 Oct 2030 reel. No swap.

## 2026-10-17 ~09:10 IST (cloud run, morning fill)
- 17-18 Oct already full. Filled Mon 19 Oct (2 days out, evergreen only):
  - 1000 mood story: "Monday hai" alarm 6 / chai 2 / motivation loading.
  - 1300 reel `delivery-wait`: 8 AM "order aaj aayega" -> nahaya nahi, gate pe baitha -> Hera Pheri "ab tak aa jaana chahiye tha" still -> 9:02 PM "Delivery attempted, customer not available". Shares: sale-season universal pain, send-to-friend.
  - 1330 teaser story of the 1300 reel.
  - 1730 carousel `monday-stages` (mascot, 7 slides): 5 min aur, 47 unread mail, meeting about a meeting, ghadi 3:34, "ab sirf 4 din aur", CTA. Shares: colleague sends on Monday itself.
  - 2100 reel `mummy-phone`: Mummy "phone rakh de" at 9 PM -> 11:40 PM light in her room -> Jethalal peeking still -> "bas ek recipe dekh rahi thi" (reel 147). Shares: siblings send to each other. Second phone/parents joke in 4 days (papa-phone 16 Oct), different angle.
  - 2130 question story: Monday 1-10 kitna bekaar.
- Trend check: X India led by Navratri/Garba (religious side, skip), World Food Day (stale). IND vs WI 5th T20I confirmed tonight 7 PM Bengaluru, already covered by 17 Oct 2030 reel. No swap.
- Analytics: 2 followers; reels get 57-106 views each, carousels near 0 reach. Kept 2 reels/day. Risk: low.
- Env note: `pip` points to a different Python here; use `python -m pip install -r requirements.txt`.
- Script: content/scripts/batch_2026-10-17.py

## 2026-10-17 ~16:05 IST (cloud run, trend check)
- Nothing missing (17-19 Oct full, 20 Oct beyond 3-day cap). Trend check: IND vs WI 5th T20I tonight 7 PM Bengaluru is a 2-2 series decider (verified), already covered by 2030 `match-vs-safai` reel. No other on-brand trend (web trending mostly music videos/news). No swap.

## 2026-10-18 ~09:05 IST (cloud run, morning fill)
- 18-19 Oct already full. Filled Tue 20 Oct (2 days out, evergreen only):
  - 1000 mood story: "Tuesday hai" Monday hangover 100% / Friday 3 din door / chai 3rd cup.
  - 1300 reel `camera-on`: boss "sab camera on karo" -> formal shirt + shorts, mummy pocha peeche -> Hera Pheri dhak-dhak still -> "Sir mera camera kharab hai" (2 saal se). Shares: WFH colleague tag.
  - 1330 teaser story of the 1300 reel.
  - 1730 image `goa-plan`: Waiting Skeleton, group chat "is baar Goa pakka", plan 2016 se. Shares: dropped straight into friend group chats.
  - 2100 reel `gym-membership`: 1 Jan resolution -> Rs 18,000 yearly -> trio shock still "gym gaya 4 baar" -> per visit Rs 4,500, gym wale ki Diwali ban gayi. Shares: tag the "kal se gym" friend.
  - 2130 question story: group ka "pakka plan" kitne saal se pending?
- Trend check: web search turned up nothing fresh/on-brand for today (IND vs WI result not findable, couldn't verify). Today/tomorrow already hold evergreen posts; no swap.
- Analytics: 3 followers; reels steady ~100 views, image/carousel ~1-2 reach, 0 shares anywhere. Kept reels-heavy. Risk: low.
- Script: content/scripts/batch_2026-10-18.py

## 2026-10-18 ~16:05 IST (cloud run, trend check)
- Nothing missing (18-20 Oct full, 21 Oct beyond 3-day cap). Trend check: headlines are SC on kids' internet access, Ramsar wetlands, defence deals, Bumrah recalled for NZ Tests (none on-brand). IND vs WI 5th T20I result still not verifiable, so skipped. No swap.

## 2026-10-19 ~09:10 IST (cloud run, morning fill)
- 19-20 Oct already full. Filled Wed 21 Oct (2 days out, evergreen only):
  - 1000 mood story: "Wednesday hai" hafta aadha gaya / energy poori gayi / 2nd chai 10 baje.
  - 1300 reel `sale-cart` (gap filler from content/backlog, oldest item): 70% off -> cart Rs 38,499 -> Hera Pheri still, balance Rs 1,240 -> remove remove remove, bacha 1 phone cover 'save for later'. Festive sales still running pre-Diwali. Shares: cart-only shopper friend.
  - 1330 teaser story of the 1300 reel.
  - 1730 image `team-player`: Trade Offer template, boss Friday 6:58 PM: Saturday 'bas 1 ghanta' ka kaam vs 'Thanks for being a team player'. Shares: colleague sends to colleague.
  - 2100 reel `appraisal-hike`: "company ka saal accha gaya" -> mann mein 30% -> 150 rupiya dega still -> hike 3%, mehngai 6%, "is saal maine company ko pay kiya". Shares: appraisal season, office group sends.
  - 2130 question story: is saal ka hike kitna aaya, ya 'process mein hai'?
- Trend check: today is Durga Ashtami (religious side, skip). IND tour of NZ starts 22 Oct (1st T20I Christchurch, verified) which is beyond the cap; worth a trend post in the 20/21 Oct 4 PM runs. No swap.
- Analytics: 3 followers, reels ~40-115 views, images ~1 reach, 0 shares. Kept reels-heavy. Risk: low.
- Env note: repo was checked out on a detached HEAD; ran `git checkout main` first.
- Script: content/scripts/batch_2026-10-19.py

## 2026-10-19 ~16:05 IST (cloud run, trend check)
- Nothing missing (19-21 Oct full, 22 Oct beyond 3-day cap). Trend check: no fresh on-brand trend found (Navratri religious side skipped). Verified IND vs NZ 1st T20I is Thu 22 Oct, Hagley Oval Christchurch, ~12:30 PM IST, so it's in office hours ("match during office lunch" angle). Queue it in the 20/21 Oct runs. No swap.

## 2026-10-20 ~16:05 IST (cloud run, trend check + fill)
- No morning entry for 20 Oct, so Thu 22 Oct was empty. Filled it:
  - 1000 mood story: "Thursday hai" match 12:30 / meeting 12:30 / kismat same.
  - 1300 reel `match-office` (scheduled-fixture post, IND vs NZ 1st T20I Thu 22 Oct, Hagley Oval, 12:30 PM IST, re-verified today): match shuru, main office mein -> excel + score + 'very productive' face -> monkey-puppet "manager peeche khada tha" -> manager: "Score kya hua?" (he was watching on mute in the 1 PM meeting). Goes live 30 min into the match. Shares: office group sends while the match is on.
  - 1330 teaser story of the 1300 reel.
  - 1730 image `ek-minute`: Jethalal 4 reactions, boss "ek minute aana zara" -> kal wala mail? / 2019 wali galti? / PIP? / resume update -> "charger hai kya?". Shares: overthinking colleague tag. (Swapped off `jethalal-thinking` template: it carries another creator's watermark, avoid it.)
  - 2100 reel `salary-mehmaan`: 10:02 salary credited -> party plans -> trio shock, 4 SMS -> EMI/rent/card/SIP, "salary 1 minute ki mehmaan thi". Shares: universal salary-day pain.
  - 2130 question story: salary account mein kitni der tikti hai?
- Trend check: today is Dussehra (religious side, skip). No other fresh on-brand trend. Backlog `for-15th-of-month` is date-specific, left in backlog. No swap.
- Analytics: 3 followers, reels ~105-123 views, carousel 1 reach, 0 shares. Kept reels-heavy. Risk: low.
- Env note: system PIL was broken; `python -m pip install --force-reinstall --ignore-installed pillow` fixed it.
- Script: content/scripts/batch_2026-10-20.py

## 2026-10-21 ~09:10 IST (cloud run, morning fill)
- 21-22 Oct already full. Filled Fri 23 Oct (2 days out, evergreen only):
  - 1000 mood story: "Friday hai" body: office mein / dil: weekend pe / kaam: Monday pe.
  - 1300 reel `doctor-stress`: doctor "stress kam lo" -> EMI kam hogi? boss badal doge? -> Hide the Pain Harold, "fees Rs 800" -> "ab stress double, dawai: 'aaram karo'". Shares: the "bas thoda stress hai" friend.
  - 1330 teaser story of the 1300 reel.
  - 1730 image `papa-at-25`: Buff Doge vs Cheems, 25 ki umar mein: Papa (ghar, scooter, 2 bachche) vs Main (3 roommates, 0 savings), footer "ek salary mein Papa ka poora ghar, meri sirf Maggi". Shares: peer-group adulting pain, tagged in roommate chats.
  - 2100 reel `papa-kitne-ka`: Papa "kitne ka liya?" -> asli Rs 4,999, bola Rs 1,200 -> 3 Idiots old man "itna mehnga?!" -> "hamare zamaane mein 40 ka aata tha", asli price batata toh main ghar ke bahar hota. Shares: universal desi kid move, very taggable.
  - 2130 question story: Papa ko kabhi kisi cheez ka ASLI price bataya hai?
- Trend check: generic India trend search returned nothing usable. Verified IND vs NZ 2nd T20I is Sat 24 Oct, Hagley Oval, ~12:30 PM IST (beyond the cap today; usable as a 'tomorrow' trend post in the 22 Oct runs). No swap: today/tomorrow already hold on-brand posts, and tomorrow's 1300 is the 1st T20I post.
- Analytics: 3 followers, reels ~50-115 views, images ~1 reach, 0 shares. Kept 2 reels + 1 image. Risk: low (papa jokes punch at the situation, not at parents).
- Env note: system PIL broken again (force-reinstalled pillow), numpy + imageio-ffmpeg needed installing.
- Script: content/scripts/batch_2026-10-21.py

## 2026-10-21 ~16:00 IST (cloud run, trend check)
- Nothing missing (21-23 Oct full, 24 Oct beyond 3-day cap). Trend check: IND vs NZ 1st T20I re-verified (Wisden: Thu 22 Oct, Hagley Oval, 20:00 local = 12:30 PM IST), already covered by tomorrow's 1300 `match-office` reel. Generic India trend search returned only undated/unreliable results. No swap.

## 2026-10-22 ~09:10 IST (cloud run, morning fill)
- 22-23 Oct already full. Filled Sat 24 Oct (2 days out, evergreen only):
  - 1000 mood story: "Saturday hai" alarm: band / body: phir bhi 6 baje uth gaya / plans: bistar.
  - 1300 reel `saturday-alarm`: weekdays alarm 7:00 snooze x5 -> Saturday no alarm, body 6 AM fresh -> Hide the Pain Harold "6 baje chhat ghoorte hue" -> "Aur Monday ko? phir 5 snooze, body ko bhi office se nafrat hai". Shares: universal, snooze-friend tag.
  - 1330 teaser story of the 1300 reel.
  - 1730 image `weekend-plan`: Gru's Plan, Sat gym/laundry -> Sun kitaab/meal prep -> "pehle bas 5 min reels" x2, footer "Sunday raat 11 baje: 'agle weekend pakka'". (First draft "uthte hi 3 baj gaye" contradicted the 1300 reel, reworked.) Shares: tag the doom-scroll friend, meta since they're watching reels.
  - 2100 reel `upi-hisaab`: "bas ek chai pe milte hai" -> 3 ghante, Rs 2,437 bill -> Jethalal evil smile -> UPI request Rs 812.50, "dosti 10 saal ki, hisaab 50 paise ka". Shares: every friend group has this guy.
  - 2130 question story: group mein 50 paise ka bhi hisaab rakhne wala dost kaun hai?
- Trend check: IND vs NZ 1st T20I today (Wisden: Hagley Oval, 20:00 local = 12:30 PM IST) already covered by today's 1300 reel. Generic trend search returned nothing usable. No swap. 2nd T20I Sat 24 Oct is a candidate to swap into the 24 Oct 1300/2100 in tomorrow's runs (24th becomes 'tomorrow').
- Analytics: 3 followers, reels ~60-120 views, images ~1 reach, 0 shares. Kept 2 reels + 1 image. Risk: low.
- Env note: detached HEAD again (checked out main); pillow/numpy/imageio-ffmpeg force-reinstalled.
- Script: content/scripts/batch_2026-10-22.py

## 2026-10-22 ~16:00 IST (cloud run, trend check)
- Nothing missing (22-24 Oct full, 25 Oct beyond 3-day cap). Trend check: IND vs NZ 1st T20I result not verifiable yet (search only gave old fixtures), generic India trend search returned nothing usable or dated. No swap. Tomorrow's runs: 2nd T20I Sat 24 Oct becomes 'tomorrow' on 23 Oct, consider swapping 24 Oct 1300/2100 evergreen reel then.

## 2026-10-23 ~09:05 IST (cloud run, morning fill + trend swap)
- Trend swap (24 Oct = tomorrow): verified IND beat NZ in the 1st T20I on 22 Oct by 4 wkts with 2 balls left, chasing 226 (Cricinfo match report), and the 2nd T20I is Sat 24 Oct, Hagley Oval, 12:30 PM IST. Moved evergreen `2026-10-24_1300_saturday-alarm-reel` + its 1330 teaser to `content/backlog/` (saturday-alarm-reel, saturday-alarm-teaser-story; reusable on any Saturday).
  - 1300 reel `salary-chase`: "India ne 226 chase kar liya" -> pressure mein bhi 2 ball pehle -> Hide the Pain Harold "aur mera chase?" -> "salary tak 7 din, Rs 1,100, required rate Rs 157/din, wicket sab gir chuke". Goes live 30 min into the 2nd T20I. Shares: month-end broke friends, cricket group chats. (Avoided match-vs-safai angle, already posted 17 Oct.)
  - 1330 teaser story of it.
- Filled Sun 25 Oct (2 days out, evergreen only):
  - 1000 mood story: "Sunday hai" mera plan: kuch nahi / mummy ka plan: sab kuch / chai: teesri.
  - 1300 reel `kya-banau`: Mummy "aaj kya banau?" -> "kuch bhi" (rajma nahi, paneer nahi, bhindi bilkul nahi) -> 3 Idiots old man "toh khud bana le" -> 1 ghante baad wahi dal chawal. Shares: universal Sunday ghar scene.
  - 1330 teaser story of the 1300 reel.
  - 1730 image `sharma-ji-jogging`: Woman Yelling at Cat, Sunday 12 baje utha toh Mummy "Sharma ji ka beta 6 baje uthta hai!" vs Main "uski salary bhi 6 guna hai", footer "comparison karna hai toh poora karo". Shares: everyone has a Sharma ji ka beta. (First render labels too cramped, shortened.)
  - 2100 reel `dhaniya-pudina`: "bas 3 cheez le aa" -> phone pe 6 aur -> Gajab bezzati -> "ye pudina hai", 25 saal ka, salary leta hu, dhaniya nahi pehchanta. Shares: taggable, light self-roast.
  - 2130 question story: sabzi lene gaye aur galat cheez laaye ho?
- Analytics: 3 followers, reels ~60-120 views, images ~1 reach, 0 shares. Kept 2 reels + 1 image. Risk: low (cricket joke is about my salary, not players; mom jokes punch at the situation).
- Env note: detached HEAD again (checked out main); pillow/numpy/imageio-ffmpeg force-reinstalled.
- Script: content/scripts/batch_2026-10-23.py

## 2026-10-23 ~16:00 IST (cloud run, trend check)
- Nothing missing (23-25 Oct full, 26 Oct beyond 3-day cap). Trend check: today's India trending results were politics (exam-leak protests), a death case and festival accident clips, all HARD LIMITS. Cricket angle already covered by tomorrow's 1300 `salary-chase` reel (2nd T20I). No swap.

## 2026-10-24 ~09:05 IST (cloud run, morning fill)
- 24-25 Oct already full. Filled Mon 26 Oct (2 days out, evergreen only, Monday office theme):
  - 1000 mood story: "Monday hai" alarm: 4 baar snooze / chai: 2 glass / energy: 9%.
  - 1300 reel `weekend-kaisa`: manager "weekend kaisa raha?" -> asli weekend (Sat 6 baje neend khuli, Sun mummy ka 'bas ek kaam', aaram 0) -> Hide the Pain Harold -> "bahut badhiya sir, fresh hu", andar se Friday ka wait shuru. Shares: office colleague tag, ties into Sat/Sun posts.
  - 1330 teaser story of the 1300 reel.
  - 1730 image `monday-buttons`: Two Buttons, Monday 7:45 AM: "Leave le lu" vs "Office jaake rou", sweating guy = Main, footer "dono mein salary same, dard alag". (First labels too small, shortened.) Shares: every Monday sick-leave drafter.
  - 2100 reel `maps-jhooth`: Maps "office 22 min" at 9:15 -> 9:40 same signal, "sabse fast route" -> waiting skeleton 10:30 -> manager "jaldi nikla karo", "sir jaldi hi nikla tha, Google Maps jhooth bolta hai". Shares: commuter group chats, no city named.
  - 2130 question story: Monday ko 'weekend kaisa raha' pe kabhi sach bola hai?
- Trend check: searches for today's trends/2nd T20I came back with stale results only. Today's 1300 `salary-chase` reel only cites the 1st T20I result, which was verified on Cricinfo yesterday, so it's safe. No swap.
- Analytics: 3 followers, reels ~105-122 views, images 1-2 reach, 0 shares. Kept 2 reels + 1 image. Risk: low.
- Env note: numpy missing again (force-reinstalled pillow/numpy/imageio-ffmpeg).
- Script: content/scripts/batch_2026-10-24.py

## 2026-10-24 ~16:00 IST (cloud run, trend check)
- Nothing missing (24-26 Oct full, 27 Oct beyond 3-day cap). Trend check: 2nd T20I (NZ 180/5, India chasing 181) still in progress with no confirmed result, and today's 1300 `salary-chase` reel already covered cricket. No swap. Env note: detached HEAD again (checked out main).

## 2026-10-25 ~09:00 IST (cloud run, morning fill)
- 25-26 Oct already full. Filled Tue 27 Oct (2 days out, evergreen only):
  - 1000 mood story: "Tuesday hai" Monday ka hangover: baaki / Friday: 3 din door / energy: 14%.
  - 1300 reel `food-fees`: app pe biryani Rs 249 -> checkout delivery/platform/packaging/small cart fee + GST -> Hera Pheri trio shock -> "Rs 412. kal se ghar ka khana", kal bhi order kiya, baaki sab meri izzat ka. No app named. Shares: everyone has stared at food-app fees.
  - 1330 teaser story of the 1300 reel.
  - 1730 image `google-doctor`: Drake, halka sa sir dard: doctor ko dikhana (no) vs Google pe symptoms padh ke 4 bimaari confirm karna (yes), footer "raat 2 baje tak will bhi likh di". Shares: tag the hypochondriac friend.
  - 2100 reel `khana-khaya`: PG raat 10 baje, Mummy "khana khaya?" -> "haan mummy, dal sabzi roti" -> Monkey Puppet, asli plate teesre din ki Maggi -> Mummy "aawaz kamzor kyu hai?", 1000 km door se Maggi pakad li. Shares: every PG/hostel kid, sibling tags.
  - 2130 question story: Mummy ko 'khana kha liya' bolke kabhi Maggi khayi hai?
- Trend check: 2nd T20I (24 Oct) result not indexed yet; generic India trend search returned nothing dated or usable. No swap.
- Analytics: 3 followers, reels ~100-120 views (24 Oct 2100 reel not counted yet), images 1 reach, 0 shares. Kept 2 reels + 1 image. Risk: low ("will likh di" is self-roast hypochondria, no real death/tragedy).
- Env note: detached HEAD again (checked out main); pillow/numpy/imageio-ffmpeg force-reinstalled with --ignore-installed.
- Script: content/scripts/batch_2026-10-25.py

## 2026-10-25 ~16:00 IST (cloud run, trend check)
- Nothing missing (25-27 Oct full, 28 Oct beyond 3-day cap). Trend check: the 2nd T20I (24 Oct) result still isn't indexed, and the generic India trend search returned nothing dated or usable. No swap. Next: Diwali (bonus/safai/sale angles) can come into the slots once it falls within today/tomorrow. Env note: detached HEAD again (checked out main).

## 2026-10-26 ~09:00 IST (cloud run, morning fill)
- 26-27 Oct already full. Filled Wed 28 Oct (2 days out, evergreen only):
  - 1000 mood story: "Wednesday hai" hafta: aadha gaya / weekend: abhi bhi door / energy: 22%.
  - 1300 reel `koi-doubt`: Sir "koi doubt?" -> "nahi sir, sab clear hai" -> Hera Pheri 'dhak dhak horela hai' -> meeting ke baad colleague ko DM "bhai kaam kya bola?", usko bhi nahi pata. Shares: office colleague tag.
  - 1330 teaser story of the 1300 reel.
  - 1730 image `theek-hu` (mascot post, brand): "Desi Dictionary: 'theek hu' ka asli matlab": theek hu = 3 din se neend nahi, bas chal raha hai = kuch nahi chal raha, busy hu = reels dekh raha hu. Shares: send to the friend who always says 'theek hu'.
  - 2100 reel `bas-5-min`: dost "bas 5 min mein pahunch raha" -> 7:45 live location abhi bhi ghar pe -> Hera Pheri 'ab tak toh usko aa jaana chahiye tha' -> 9 baje "bhai traffic tha", nahane hi 8 baje gaya. Shares: every friend group's late guy.
  - 2130 question story: group mein 'bas 5 min' bolke 1 ghanta lagane wala kaun hai?
- Trend check: Diwali 2026 is 8 Nov (adhik maas year, Drik Panchang per search), so bonus/safai/sale angles are not today/tomorrow yet. IND vs NZ 3rd T20I is Tue 27 Oct (Wellington); start time and 2nd T20I result not verifiable in search, cricket already had 2 reels. No swap.
- Analytics: 3 followers, reels ~95-110 reach (24-25 Oct 2100 reels not counted yet), images 1 reach, 0 shares. Kept 2 reels + 1 image, made the image a mascot post. Risk: low.
- Env note: detached HEAD again (checked out main); pillow/numpy/imageio-ffmpeg force-reinstalled with --ignore-installed.
- Script: content/scripts/batch_2026-10-26.py

## 2026-10-26 ~16:00 IST (cloud run, trend check)
- Nothing missing (26-28 Oct full, 29 Oct beyond 3-day cap). Trend check: generic India trend search returned only undated/unreliable pages; IND vs NZ 2nd T20I result still not indexed, 3rd T20I is tomorrow but start time unverifiable. Diwali (8 Nov) still too far for today/tomorrow. No swap. Env note: detached HEAD again (checked out main).

## 2026-10-27 ~09:00 IST (cloud run, morning fill)
- 27-28 Oct already full. Filled Thu 29 Oct (2 days out, evergreen only):
  - 1000 mood story: "Thursday hai" Friday: bas kal / salary: 3 din door / energy: 31%.
  - 1300 reel `cab-cancel`: office cab 'driver 2 min away' -> 15 min baad ab bhi 2 min away -> ride cancel, Panchayat 'Dekh raha hai na Binod' -> cancel usne kiya, cancellation fee mujhse kati, late mark bhi mujhe. No app named. Shares: commute reels are our best (maps-jhooth 208 views), office colleague tag.
  - 1330 teaser story of the 1300 reel.
  - 1730 image `budget-clown`: Clown Applying Makeup, "Har mahine ka budget plan": paise bachaunga / Excel sheet bana di / bas ek chhota sa order / 29 tareekh: Rs 312 bache, footer "Excel mein savings, account mein clown". Posts on the 29th itself. Shares: the 'is mahine pakka bachaunga' friend. (Relabelled last line + mood story for cleaner wraps.)
  - 2100 reel `bas-ek-episode`: raat 11 'bas ek episode' -> 1:30 AM 'next episode in 5' -> 3 AM Roll Safe 'soya hi nahi toh late kaise uthunga' -> 9:30 standup 'kal kya kiya?' 'research'. No show named. Shares: binge-watcher friend tag.
  - 2130 question story: 'bas ek episode' bolke sabse late kitne baje soye ho?
- Trend check: IND vs NZ 3rd T20I / generic India trends for today not verifiable in search (only old results). No swap. Backlog (15-taareekh carousel, Saturday alarm reel) doesn't fit Thursday, left there.
- Analytics: 3 followers, reels ~100-200 views (26 Oct maps-jhooth 208, best so far), images 0-1 reach, 0 shares. Leaning into commute/office reels. Risk: low (cab joke punches at the situation, not drivers).
- Env note: `pip` points to py3.13 while `python` is 3.11; used `python -m pip install --ignore-installed pillow numpy imageio-ffmpeg`.
- Script: content/scripts/batch_2026-10-27.py

## 2026-10-27 ~16:00 IST (cloud run, trend check)
- Nothing missing (27-29 Oct full, 30 Oct beyond 3-day cap). Trend check: generic India trend search and IND vs NZ 3rd T20I search returned only old results (2019-2023), nothing verifiable for today. Today's 2100 `khana-khaya` reel stays. No swap. Env note: detached HEAD again (checked out main).

## 2026-10-28 ~09:00 IST (cloud run, morning fill)
- 28-29 Oct already full. Filled Fri 30 Oct (2 days out, evergreen only):
  - 1000 mood story: "Friday hai" weekend: 6 baje / kaam: Monday / energy: 9%.
  - 1300 reel `pahunch-ke-call`: Mummy 'pahunch ke call karna' -> phone silent, bhool gaya, 3 ghante -> 23 missed calls, Hera Pheri 'dhak dhak' -> call back: 'pahunch gaya?' 'haan', phir 40 min lecture 'call karna' pe. Shares: the friend who never calls after reaching (parents reels do ~120-170 views).
  - 1330 teaser story of the 1300 reel.
  - 1730 image `bank-trade-offer`: Trade Offer, "Month end pe bank ka trade offer": i receive Rs 590 'minimum balance' charge / you receive ek SMS 'Dear Customer', footer "Balance minimum, charge maximum". No bank named. Posts on the 30th (month end). Shares: the 3-digit-balance friend.
  - 2100 reel: gap filler from backlog, `saturday-alarm` (weekday 5 snoozes vs Saturday 6 AM wide awake). Fits Friday night. Its old teaser story stays in backlog (1330 teaser goes to the new 1300 reel).
  - 2130 question story: Saturday ko bina alarm ke kitne baje uth jaate ho? (ties to the 2100 reel)
- Trend check: generic India trend search returned only template/spam pages, nothing dated or verifiable. No swap.
- Analytics: 3 followers, reels ~100-200 views (biryani-fees 167, maps-jhooth 208), images still 0-1 reach and 0 shares across the board. Kept 1 image/day per routine, but images look close to zero distribution; worth the owner checking. Risk: low.
- Env note: `python -m pip install --ignore-installed pillow numpy imageio-ffmpeg` needed again.
- Script: content/scripts/batch_2026-10-28.py

## 2026-10-28 ~16:00 IST (cloud run, trend check)
- Nothing missing (28-30 Oct full, 31 Oct beyond 3-day cap). Trend check: headlines today = exam paper-leak protests/minister resignation (politics, hard limit), cyclone Arnab on Andhra coast (disaster, hard limit), Jio IPO listing (only one headline, not verifiable with a date, and centres on a real businessman: skipped), IND sealed T20I series vs NZ (cricket already done twice, 4th T20I 30 Oct per single source). Today's 2100 `bas-5-min` reel stays. No swap.

## 2026-10-29 ~09:00 IST (cloud run, morning fill)
- 29-30 Oct already full. Filled Sat 31 Oct (2 days out, evergreen only):
  - 1000 mood story: "Saturday hai" alarm: band / plan: kuch nahi / energy: 40%.
  - 1300 reel `udhaar-dost`: 6 mahine se gayab dost 'bhai kaisa hai, bahut yaad aayi' -> main: shayad mera Rs 2000 lautayega -> Phir Hera Pheri 'Paisa laya?' -> 'bhai 3000 de de', purane 2000 ka zikr bhi nahi. First use of paisa-laya. Shares: everyone has an udhaar friend to tag.
  - 1330 teaser story of the 1300 reel.
  - 1730 image `alternate-saturday`: Two Guys on a Bus (first use), "Saturday subah 9 baje": main alternate Saturday working (rock side) / dost 'bhai brunch chalein?' (sunny side). Shares: colleague tag.
  - 2100 reel `saturday-raat`: dost 'aaj bahar chalte hai' -> Buff Doge vs Cheems 18 vs 26 -> 9:30 khichdi, lights band, 'bas 5 min' -> 2:47 AM still awake, bas bina mazze ke. Shares: the 'thak gaya hu bhai' friend.
  - 2130 question story: Saturday raat: bahar party ya ghar pe khichdi + reels? (ties to 2100 reel)
- Trend check: search returned only undated/template pages, nothing verifiable for today. Today's 2100 `bas-ek-episode` stays. No swap. Backlog untouched.
- Analytics (28 Oct night): 3 followers, 1300 reels steady ~110-210 views, but several 2100 reels show 0 reach (24, 25, 28 Oct) and images still 0-1 reach. 28 Oct 2100 may just be too fresh; 24/25 Oct zeros worth the owner checking (publish/insights issue vs real). Risk: low.
- Env note: detached HEAD again; `python -m pip install --ignore-installed pillow numpy imageio-ffmpeg` needed again.
- Script: content/scripts/batch_2026-10-29.py

## 2026-10-29 ~16:00 IST (cloud run, trend check)
- Nothing missing (29-31 Oct full, 1 Nov beyond 3-day cap). Trend check: generic India trend search gave only undated/spam pages. Verified IND vs NZ 4th T20I is Fri 30 Oct, Eden Park, 12:30 PM IST (Wisden/ESPN fixtures). Office-hours-match angle already used (22 Oct `match-office` reel), series already sealed, so it's not worth swapping out tomorrow's evergreen `pahunch-ke-call` reel. Today's 2100 `bas-ek-episode` stays. No swap, backlog untouched.

## 2026-10-30 ~09:00 IST (cloud run, morning fill)
- 30-31 Oct already full. Filled Sun 1 Nov (2 days out, evergreen only; also 1st of the month):
  - 1000 mood story: "1 tareekh + Sunday" naya mahina: shuru / naya main: kal se / energy: 30%.
  - 1300 reel `naya-mahina`: "Naya mahina, naya main" -> plan (6 baje uthna, gym, budget, ghar ka khana) -> Raju confident pose (first use of raju-waiting-pose) -> "Aaj toh Sunday hai. Naya main kal se. Waise 10 mahine se 'kal se' hi hai". Shares: the 'is baar serious hu' friend.
  - 1330 teaser story of the 1300 reel.
  - 1730 image `sunday-presentation`: They Don't Know (first use), "Sunday shaam family ke saath hasta hua main. Inhe nahi pata kal 10 baje wali presentation ki ek slide bhi nahi bani", footer "Chehra Sunday, dimaag Monday". Label zone overlapped the figure's head, so the joke moved into the caption band. Shares: colleague tag.
  - 2100 reel `pakka-plan`: group chat 'is Sunday pakka milte hai' -> 'thoda late / shayad nahi / seen' -> Hera Pheri 'ab tak toh aa jaana chahiye tha' -> 'next Sunday pakka', group name 'Goa Plan 2019'. Shares: built to be dropped into friend groups.
  - 2130 question story: tumhare group ka 'pakka plan' last kab sach mein hua tha? (ties to 2100 reel)
- Trend check: search returned only undated/spam pages and January IND vs NZ results, nothing verifiable for today. Today's 2100 `saturday-alarm` stays. No swap, backlog untouched.
- Analytics (29 Oct night): still 3 followers. 1300 reels steady ~110-210 views, 2100 reels keep showing 0 reach (24, 25, 28, 29 Oct), images 0-1 reach, 0 shares on everything. The 2100 zeros look systematic, not random: owner should check whether evening reels actually go live/distribute (or move the second reel earlier, e.g. 1800). Risk: low.
- Script: content/scripts/batch_2026-10-30.py

## 2026-10-30 ~16:00 IST (cloud run, trend check)
- Nothing missing (30 Oct-1 Nov full, 2 Nov beyond 3-day cap). Trend check (Trends24/twitter-trending, 29 Oct snapshots): Karwa Chauth (festival whose jokes centre on the fast/ritual side: skipped), Jio IPO listing / Ambani family (real people: skipped), Bigg Boss 20 contestants (real people: skipped), plus political hashtags. IND vs NZ 4th T20I today already ruled out yesterday. Today's 2100 `saturday-alarm` stays. No swap, backlog untouched.

## 2026-10-31 ~09:00 IST (cloud run, morning fill)
- 31 Oct-1 Nov already full. Filled Mon 2 Nov (2 days out, evergreen only):
  - 1000 mood story: "Monday + 2 tareekh" salary: aa gayi / motivation: nahi aayi / energy: 15%.
  - 1300 reel `friday-kya-kiya`: Monday standup, manager 'Friday kya kiya tha?' -> dimaag: sirf 5:59 pe laptop band kiya yaad hai -> Monkey Puppet (first use) -> "'Sir, pending items pe tha'. Kaunse items? Wo bhi pending hai". Shares: colleague tag on a Monday.
  - 1330 teaser story of the 1300 reel.
  - 1730 image `ek-minute-kaam`: Epic Handshake (first use), Mummy x Manager agreeing on "'Bas ek minute ka kaam hai'", footer "Ek minute = 2 ghante". Shares: mom + office crossover, very taggable.
  - 2100 reel `ghar-ka-it-support`: Papa 'office mein karte kya ho?' -> 'cloud migration, stakeholder alignment' -> Hera Pheri trio shock -> "Papa: 'accha, toh printer theek kar do'. 3 saal se ghar ka IT support bhi main hu". Shares: every desi techie's family story.
  - 2130 question story: ghar walo ko tumhari job kya lagti hai? (ties to 2100 reel)
- Trend check: search returned only undated/spam pages, nothing verifiable for today. Today's 2100 `saturday-raat` stays. No swap, backlog untouched.
- Analytics (30 Oct night): still 3 followers, 0 shares on everything. 1300 reels ~100-140 views; 30 Oct 2100 reel got 118 views, so the 2100 zero-reach pattern broke once. Images still 0 reach. Risk: low.
- Env note: `python -m pip install --ignore-installed pillow numpy imageio-ffmpeg` needed again.
- Script: content/scripts/batch_2026-10-31.py

## 2026-10-31 ~16:00 IST (cloud run, trend check)
- Nothing missing (31 Oct-2 Nov full, 3 Nov beyond 3-day cap). Trend check: generic India search gave only undated/spam pages. Verified IND vs NZ 5th T20I is Sun 1 Nov, Seddon Park, 12:30 PM IST (Wisden/ESPN fixtures), but the series is already sealed and cricket angles were used twice, so it's not worth swapping tomorrow's evergreen `naya-mahina` reel (1st of month fits better). Halloween skipped (weak desi fit). Today's 2100 `saturday-raat` stays. No swap, backlog untouched.

## 2026-11-01 ~09:00 IST (cloud run, morning fill)
- 1-2 Nov already full. Filled Tue 3 Nov (2 days out, evergreen only):
  - 1000 mood story: "Tuesday hai" Monday ka excuse: khatam / Friday: abhi bahut door / energy: 20%.
  - 1300 reel `6-baje-nikalna`: 5:55 'aaj 6 baje pakka nikal raha hu' -> plan 5:57/5:58/5:59 -> Phir Hera Pheri trio running (first use) -> lift mein manager: 'perfect timing, quick call walk karte hue', ghar 9:40. Shares: colleague tag.
  - 1330 teaser story of the 1300 reel.
  - 1730 image `naya-course`: Distracted Boyfriend (first use), "Mera har mahine ka self improvement": main eyeing naya course 'AI seekho 30 din mein' over pichhle 7 courses (12% done), footer "Cart full, completion 0%". No platform named. Shares: the 10-adhure-courses friend.
  - 2100 reel `shaadi-mein-fasa`: relative ki shaadi 'bas 10 min' -> aunty: package kitna / itna hi / Sharma ji ka beta -> Welcome Dr Ghunghroo sofa (first use) -> "'Aur shaadi kab kar rahe ho?'" khana laga nahi, 10 min = 2 ghante. Wedding season (Nov) but no festival/religious angle. Shares: relatives pain, tag the unmarried friend.
  - 2130 question story: shaadi mein relatives ka sabse irritating sawaal? (ties to 2100 reel)
- Trend check: search returned only undated/spam pages, nothing verifiable for today. Today's 2100 `pakka-plan` stays. No swap, backlog untouched.
- Analytics (31 Oct night): still 3 followers, 0 shares on everything. All three 31 Oct posts show 0 reach, including the 1300 reel (1300 reels had been steady ~100-170). Could be insights lag, but if 1 Nov's snapshot shows it again the owner should check the account (possible distribution drop). Risk: low.
- Env note: detached HEAD again; `python -m pip install --ignore-installed pillow numpy imageio-ffmpeg` needed again.
- Script: content/scripts/batch_2026-11-01.py

## 2026-11-01 ~16:00 IST (cloud run, trend check)
- Nothing missing (1-3 Nov full, 4 Nov beyond 3-day cap). Trend check: generic India search gave only calendar/undated pages; the IND vs NZ 5th T20I result couldn't be verified (only older series came up), so no cricket swap. Ahoi Ashtami today is religious, so skipped. Today's 2100 `pakka-plan` stays. No swap, backlog untouched.
- Heads-up for the next fills: search results say Diwali is Sun 8 Nov 2026 (re-check before using). Diwali gift/safai/bonus jokes already ran 15-17 Oct, so use fresh angles only (sale cart, last-day leave, relatives' visits, post-Diwali Monday) in the 6-8 Nov slots.
- Analytics: latest.json is still the 31 Oct snapshot (no newer nightly refresh). Still 3 followers and 0 reach on all of 31 Oct's posts, so the possible distribution drop is unconfirmed but still worth the owner checking.

## 2026-11-02 ~09:00 IST (cloud run, morning fill)
- 2-3 Nov already full. Filled Wed 4 Nov (2 days out, evergreen; Diwali-week leave is a fixed-date office angle, not a trend):
  - 1000 mood story: "Wednesday hai" Diwali chutti: pending / kaam: double / energy: 25%.
  - 1300 reel `diwali-leave`: 'Sir, 6 se 9 chutti chahiye' -> manager 'saari team ek saath chutti pe? deadline?' -> Panchayat Bhushan (first use) as manager ka dimaag -> "Chutti approve ho gayi. 'Bas laptop ghar le jaana, emergency ke liye.' Emergency roz 11 baje". Office/leave only, no religious side. Shares: every colleague waiting on Diwali leave approval this week.
  - 1330 teaser story of the 1300 reel.
  - 1730 image `busy-dikhna`: Expanding Brain (first use), "Office mein busy dikhne ke tareeke": kaam karo -> Excel khula rakho -> mouse hilate raho, green dot on -> 'offline lete hai' bolo, footer "Promotion bhi offline hi hai". Shares: colleague tag.
  - 2100 reel `papa-forward`: Papa ka 7 AM family group forward ('3 glass garam paani, 100 saal, doctor bhi shocked') -> 'Papa ye fake hai' -> Abba nahi manenge (first use) -> "'Tumse zyada padha hua hu'. Forward 4 aur groups mein gaya, ab mujhe bhi 3 glass paani". Harmless made-up health forward, no politics/religion. Shares: siblings sharing family-group pain.
  - 2130 question story: family group ka sabse best forward? (ties to 2100 reel)
- Trend check: generic India search gave only undated/spam pages, nothing verifiable. Diwali re-verified as Sun 8 Nov 2026 (multiple panchang sources). Today's 2100 `ghar-ka-it-support` stays. No swap, backlog untouched.
- Analytics (1 Nov night): still 3 followers, 0 shares on everything. 1 Nov reels recovered (1300: 145 views, 2100: 108 views) so the 31 Oct zero looks like a one-off. Images stay at ~1 reach every day: the 1730 image slot is basically dead; owner may want to swap it for a third reel or carousel. Risk: low.
- Env note: detached HEAD again; pillow/numpy/imageio-ffmpeg reinstall needed again.
- Script: content/scripts/batch_2026-11-02.py

## 2026-11-02 ~16:00 IST (cloud run, trend check)
- Nothing missing (2-4 Nov full, 5 Nov beyond 3-day cap). Trend check: generic India search gave only undated/spam pages; one source lists an IND vs NZ ODI on Wed 4 Nov (Eden Park) but it's single-sourced and unverified, and Wed 4 Nov's slots already hold the Diwali-leave/office set, so no cricket swap. Today's 2100 `ghar-ka-it-support` stays. No swap, backlog untouched.

## 2026-11-03 ~09:00 IST (cloud run, morning fill)
- 3-4 Nov already full. Filled Thu 5 Nov (2 days out, evergreen only):
  - 1000 mood story: "Thursday hai" Friday: kal / kaam: aaj hi chahiye / energy: 30%.
  - 1300 reel `raat-ka-message`: Boss 10:47 PM 'are you there?' -> reply/nahi/seen dilemma -> Hera Pheri Babu Bhaiya 'Bilkul risk ne lene ka' (first use) -> "'Sorry sir, so gaya tha'. Sach: raat bhar phone ghoorta raha". Shares: colleague tag, every desi with a late-night-texting boss.
  - 1330 teaser story of the 1300 reel.
  - 1730 image `salary-pigeon`: Is This A Pigeon (first use), "Har mahine 5 tareekh ko": Main / Salary ka SMS / "Kya ye savings hai?", footer "Nahi beta, ye EMI ka hai". Shares: salary/EMI pain, tag the 'is baar bachaunga' friend.
  - 2100 reel `5-saal-baad`: Interview 'where do you see yourself in 5 years?' -> 'leadership role, growth hi growth' -> Hide the Pain Harold as 5 saal baad -> "Same company, same chair. Title mein 'Senior' lag gaya, salary ne interview suna hi nahi". Shares: colleague tag.
  - 2130 question story: interview mein sabse bada jhooth kya bola tha?
- Trend check: generic India search gave only undated/spam pages, nothing verifiable. Today's 2100 `shaadi-mein-fasa` stays. No swap, backlog untouched.
- Analytics (2 Nov night): still 3 followers, 0 shares on everything. Reels steady ~110-130 views, 1730 images still reach 1. Kept the image slot per ROUTINE.md, but the owner should decide on replacing it with a third reel. Risk: low.
- Env note: detached HEAD again; background pip install hung, a foreground reinstall of pillow/numpy/imageio-ffmpeg worked.
- Script: content/scripts/batch_2026-11-03.py

## 2026-11-03 ~16:00 IST (cloud run, trend check)
- Nothing missing (3-5 Nov full, 6 Nov beyond 3-day cap). Trend check: generic India search gave only undated/spam pages. Verified IND vs NZ 1st ODI is Wed 4 Nov, Eden Park, ~7:30 AM IST (Outlook/Khel Now/ESPN agree). Not swapped: the match ends ~3:30 PM IST with an unknown result, so tomorrow's 2100 `papa-forward` would need a result-based joke we can't write yet; the 1300 slot is the fixed-date `diwali-leave` reel; cricket angles already used twice. Possible angle for a later ODI (7/10 Nov, morning IST start): "office meeting mein chupke se score check". Today's 2100 `shaadi-mein-fasa` stays. No swap, backlog untouched.

## 2026-11-04 ~09:00 IST (cloud run, morning fill)
- 4-5 Nov already full. Filled Fri 6 Nov (2 days out, evergreen; Diwali-week travel/leave are fixed-date angles, no religious side):
  - 1000 mood story: "Friday hai" weekend: aa raha / kaam: abhi bhi pending / energy: 40%.
  - 1300 reel `tatkal-ticket`: 10:00:00 AM tatkal khula, ghar jaana hai -> captcha galat/OTP late/payment loading -> Phir Hera Pheri Raju laughing (first use) as 'wo dost jisne 2 mahine pehle book kiya' -> "Status: WL 247. Bus wala 3 guna fare, is baar ghar sirf video call pe". AC tatkal 10 AM checked (multiple guides, not official IRCTC). Shares: everyone travelling home this week, tag the planner friend.
  - 1330 teaser story of the 1300 reel.
  - 1730 image `aadhi-team-chutti`: Squidward Window (first use), "Diwali wala Friday: aadhi team gayab", footer "Mera leave request: abhi bhi 'pending'". Shares: colleague tag, the one already on leave.
  - 2100 reel `monday-quick-call`: Friday 5:58 PM manager 'Monday quick call, kuch discuss karna hai' -> weekend overthinking (galti? appraisal? layoff?) -> This Is Fine (as Sunday raat 2 baje) -> "Monday 10 baje: 'team lunch Wednesday ko rakh le?'". Shares: universal office anxiety, colleague tag.
  - 2130 question story: manager ka sabse darawna message kya hai? (ties to 2100 reel)
- Trend check: generic India search gave only undated/spam pages. IND vs NZ 1st ODI is on now (result after ~3:30 PM IST), left for the 4 PM run to judge a swap of today's 2100 `papa-forward`. No swap, backlog untouched.
- Analytics (3 Nov night): still 3 followers, 0 shares on everything. Reels steady ~105-135 views, 1730 images still reach 1. Image slot kept per ROUTINE.md; owner decision on a third reel still open. Risk: low.
- Env note: detached HEAD again; pillow/numpy/imageio-ffmpeg reinstall needed again.
- Script: content/scripts/batch_2026-11-04.py

## 2026-11-04 ~16:00 IST (cloud run, trend check)
- Nothing missing (4-6 Nov full, 7 Nov beyond 3-day cap). Trend check: IND vs NZ 1st ODI (Eden Park, today) result not indexed yet; the only "India win by 4 wickets" hits were the Jan 2026 Vadodara ODI, so no verified result to joke on. Generic India search gave only undated/spam pages. Today's 2100 `papa-forward` stays. No swap, backlog untouched.

## 2026-11-05 ~09:00 IST (cloud run, morning fill)
- 5-6 Nov already full. Filled Sat 7 Nov (2 days out, evergreen; day before Diwali but no festival angle used):
  - 1000 mood story: "Saturday hai" neend: abhi bhi kam / mummy ka khaana: full / energy: 60%.
  - 1300 reel `patla-mota`: Ghar pahunchte hi mummy 'kitna patla ho gaya' -> 4 paratha, 2 katori kheer, 'bas ek aur' -> Welcome Uday Shetty (first use) as Papa teesre din -> "'Itna mota kaise ho gaya?' Same beta, same hafta". Shares: everyone home for the holidays, tag the friend who comes back 3 kilo heavier.
  - 1330 teaser story of the 1300 reel.
  - 1730 image `linkedin-thrilled`: 3 Idiots Chatur speech (first use), "LinkedIn pe main: 'Thrilled to share, new role started!'", footer "Asli mein: same kaam, naya Excel". Shares: colleague tag.
  - 2100 reel `mummy-free-ho`: Mummy 'free ho toh call karna, ek baat batani hai' -> panic -> Jethalal thinking 4-panel (koi bimaar? paise? rishta? result?) -> "Call pe mummy: 'Wo Netflix ka password kya tha? TV maang raha hai'". Shares: universal mummy-message anxiety, IT-support kid.
  - 2130 question story: mummy ka sabse darawna message kya hota hai? (ties to 2100 reel)
- Trend check: IND vs NZ 1st ODI (4 Nov) result still not indexed (search only returns Jan 2026 / older matches), nothing else verifiable. Today's 2100 `5-saal-baad` stays. No swap, backlog untouched.
- Analytics (4 Nov night): still 3 followers, 0 shares/saves on everything. Reels ~80-130 reach (2100 papa-forward dipped to 82), 1730 images still reach 1. Image slot kept per ROUTINE.md; owner decision on a third reel still open. Risk: low.
- Env note: detached HEAD again (checked out main from origin); pillow/numpy/imageio-ffmpeg reinstall needed again.
- Script: content/scripts/batch_2026-11-05.py

## 2026-11-05 ~16:00 IST (cloud run, trend check)
- Nothing missing (5-7 Nov full, 8 Nov beyond 3-day cap). Trend check: generic India search gave only undated/spam pages; IND vs NZ 1st ODI (4 Nov) result still not indexed (only Jan 2026 Vadodara hits). Nothing verified to joke on. Today's 2100 `5-saal-baad` and tomorrow's slots stay. No swap, backlog untouched.

## 2026-11-06 ~09:00 IST (cloud run, morning fill)
- ALERT: 5 Nov 1730 image `salary-pigeon` was published 3 TIMES on Instagram (12:00/12:01/12:02 UTC, 3 media ids in analytics) and the folder still ended up in `content/failed/`. Looks like the publisher retried after a false failure. Owner should delete 2 duplicates manually and check the publish logs; not touching publish code per ROUTINE.md.
- 6-7 Nov already full. Filled Sun 8 Nov (Diwali day, verified again; only soan papdi/relatives/chutti angles, no religious side):
  - 1000 mood story: "Diwali Sunday ko" extra chutti: 0 / relatives: aane wale / energy: 50%.
  - 1300 reel `soan-papdi`: Soan papdi ka ek dabba -> route map padosi aunty -> hum -> mama ji -> chachi -> Monkey Puppet "5 din baad, doorbell" -> "Wahi dabba wapas aaya, sticker pe humari handwriting, kisi ne khola tak nahi". Shares: every desi house with 4 dabbe pending.
  - 1330 teaser story of the 1300 reel.
  - 1730 image `package-kitna`: 3 Idiots interview 'salary kitni' (first use), "Diwali pe chacha ji, mithai se bhi pehle:", footer "'Toh beta, package kitna hai ab?'". Shares: tag the friend whose package the whole khandaan learns today.
  - 2100 reel `diwali-sunday`: "Is saal Diwali kis din? Sunday." -> extra chutti 0 / bonus 'next quarter' / kal 9:30 standup -> Panchayat 'Gajab bezzati' as office group chat -> Monday manager "Hope everyone had a restful long weekend! Kaunsa long, sir?". Shares: colleague tag on Diwali night.
  - 2130 question story: aaj relatives ne sabse darawna sawaal kya pucha?
- Trend check: IND vs NZ 1st ODI (4 Nov) result still not indexed; 2nd ODI is Sat 7 Nov (Wellington). No swap, backlog untouched.
- Analytics (5 Nov night): still 3 followers, 0 shares/saves. Reels steady ~100-120 reach, images reach 1. Risk: low.
- Env note: detached HEAD; `python` (3.11) has a broken PIL, used `python3.13` which has pillow/numpy/imageio-ffmpeg.
- Script: content/scripts/batch_2026-11-07.py

## 2026-11-06 ~16:00 IST (cloud run, trend check)
- Nothing missing (6-8 Nov full, 9 Nov beyond 3-day cap). Trend check: IND vs NZ 1st ODI (4 Nov) result still not indexed (only Jan 2026 Vadodara hits); generic India search gave only undated/old pages. Nothing verified to joke on. Today's 2100 `monday-quick-call` and tomorrow's slots stay. No swap, backlog untouched. Duplicate `salary-pigeon` alert from the morning run still stands for the owner.

## 2026-11-07 ~09:00 IST (cloud run, morning fill)
- 7-8 Nov already full. Filled Mon 9 Nov (2 days out, evergreen; 8 Nov 2100 already does the Monday-after-Diwali manager joke, so no repeat):
  - 1000 mood story: "Chutti ke baad Monday" neend: ghar pe chhoot gayi / inbox: 214 unread / energy: 10%.
  - 1300 reel `mummy-ka-bag`: Mummy 'bas thoda sa pack kiya hai' -> 2 kilo laddoo, 3 dabbe achaar, 1 litre ghee -> Phir Hera Pheri 'Abhi maza ayega na bhidu' (first use) as airport counter wala -> "Bag 23 kg: 4 kg kapde, 19 kg mummy ka pyaar, extra baggage Rs 3,400". Shares: everyone heading back to the city after the holidays, tag the friend with the ghee bag.
  - 1330 teaser story of the 1300 reel.
  - 1730 image `meeting-ka-agenda`: Panchayat office meeting (first use), "Monday 10 baje ki meeting jo ek mail ho sakti thi:", footer "Agenda: agli meeting kab rakhein". Shares: colleague tag.
  - 2100 reel `3-baje-meeting`: post-lunch 3 PM meeting, aankhein band / camera on -> Welcome scene (first use) for 'any thoughts, team?' -> "Maine bola 'agreed sir', baad mein pata chala wo task ab mera hai". Shares: tag the camera-on sleeper.
  - 2130 question story: mummy ne is baar bag mein sabse ajeeb cheez kya pack ki? (ties to 1300 reel)
- Trend check: IND vs NZ 2nd ODI (7 Nov) not indexed, search only returns Jan 2026 / older series. Nothing verified. No swap, backlog untouched.
- Analytics (6 Nov night): still 3 followers, 0 shares/saves. Reels ~100-130 views, 1730 images reach 1. Duplicate `salary-pigeon` (3 posts) still live, owner action pending. Risk: low.
- Script: content/scripts/batch_2026-11-09.py

## 2026-11-07 ~16:00 IST (cloud run, trend check)
- Nothing missing (7-9 Nov full, 10 Nov beyond 3-day cap). Trend check: IND vs NZ 2nd ODI (Wellington, 7 Nov) result not indexed (search only returns Jan 2026 Rajkot / older series). Nothing verified to joke on. Today's 2100 `mummy-free-ho` and tomorrow's Diwali slots stay. No swap, backlog untouched. Duplicate `salary-pigeon` alert still pending for the owner.
