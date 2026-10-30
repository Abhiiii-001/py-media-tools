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
