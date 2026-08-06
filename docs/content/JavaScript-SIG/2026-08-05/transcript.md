SIG: JavaScript SIG
Date: 2026-08-05
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Trent Mick** 00:55 Hello?
**Abhinav Mathur** 01:00 -Oh.
**Trent Mick** 01:02 So heads up, there are a number of people on vacation this week, so this might be a super light one. We'll see who turns up in a few minutes.
**Abhinav Mathur** 01:09 I see you, okay.
I'm not sure why August is such a special month, though.
I guess,
**Trent Mick** 01:17 Kids are off school, and it's way too hot in some places like Barcelona, so people go on vacation now, right?
**Abhinav Mathur** 01:22 I see, okay, makes sense.
**Trent Mick** 01:37 David, I have some friends who are just coming back today from… Part of their vacation in Barcelona. Seems like a crazy time to go visit there.
Isn't it? What's it like there, right now?
**David Luna Bistuer** 01:54 Hello?
**Trent Mick** 02:00 Alright, hello, everyone, like, people. Maybe we'll get started. 5 is actually… More than I expected this week, given vacations, so… That's the right window.
Group size a little bit.
**Jamie Danielson** 02:21 Yeah, we see the duck.
**Trent Mick** 02:35 Okay, please, Zephyr at… Some topics as we go below, I rarely run this, and oh boy, I can't think on my feet, so probably not going to be doing a triage at the end, but I noticed we had a couple P1s, one in each repo that came up in the last week or so, so maybe we'll take a look at those, if people haven't, or even mainly to point them out. And then… We'll close early, probably. Okay, so… for other people following along, this is Matt's… PR from a few weeks ago that I'd said I'd follow up on again. There'd been an early VR, this for declarative config work, and adding a config provider, which is kind of a later addition to the declarative config spec.
Anyway, this is on me to take a look at, or at least I intend to, it'd be great if other people want to as well.
Yeah.
David, entities, you want to take 15 minutes and explain it to us?
I've lost the plot.
**David Luna Bistuer** 03:46 15 or 50?
Yeah.
**Trent Mick** 03:50 Yes.
**David Luna Bistuer** 03:51 Okay, this could be… okay, okay, hi, everyone. So, It's a lot to explain, but, long story short, so maybe in Browser B, might be willing to tackle this on the specification, and maybe make a proposal for browser.
But at least the use cases that we are proposing in the processing, or at least It seems to me, so that's my opinion, my… My observation, so it makes more sense to have entities on… on… Browser or clients.
That may be on the backend servers.
For example, we have sessions, we have pages, we have user sessions, we have different things that may change over time, so they don't follow the lifecycle of the SDK.
So yeah.
**Trent Mick** 04:41 Have a resource, you need.
**David Luna Bistuer** 04:42 Yeah, exactly. So, and there have been a couple of proposals, I think that Daniel already made a… a draft PR on… on entities, and then there is another one from Martin in Roger that it's kind of following the same pattern.
Which is the… to… So, they may… they are making it at a provider level, so you have a provider, like, I'll say, a larger provider, and then you have an API. Anything is part of the spec that you, you can, you can say that you wanna… specific provider for this entity, then it gives you back another provider, which… Merges the entity information with the resource, with the actual… with the original resource, and so on.
Well, since we are tackling sessions and so on, maybe in browser we are going to, Start to discuss this, and maybe make a proposal.
I don't know what… which is the appetite, or… We're willing to review that and make it maybe, have a look and give it a thumbs up for note.
Or maybe that could be a thing that could deviate from what is browser and… And… and Node.js.
So, thoughts on that? So… Anyone that thinks about the use case in… or entities in… Nordland.
**Trent Mick** 06:14 So, I mean, I think if it's in the spec, then we should do it. I'm not clear… I can't… I haven't followed closely enough to know what's landed in spec and what hasn't. I know the… hotel spec and maintainer SIG earlier this week had it on the agenda, and they were talking about it, but I had to drop out of that call, so I missed that.
I mean, I think if it's spec-level stuff, then we probably want it for Node, and it'd be nice if… Not in browser.
base implementation is… is the same there. Like, is this something that would land in… one of the core packages that we'd want. I like… I don't… Browser has the better use case for it right now, so maybe… maybe it goes that way. I know for sure that I'd want Dan to have an opinion on that, because he's been more involved in the entities side, both on the spec end, doing node… for POCs, so… I assume he'll have a stronger opinion, or more educated one.
**David Luna Bistuer** 07:15 Okay. I've seen the… so, for example, one of the things that, for us was not a stopper, but… Made us hesitate on that is… We have high cardinality when it comes from entities, specifically for page.
at, you know, web application updates got changed a lot. Specifically, we are recording the UR and the free URL, so query params and all this kind of stuff.
And… this is kind of a… Stopper for metrics, so you have, high cardinality of metrics since… It's something that is not good.
Hmm… Core resolution, though, is just to have a processor to add information related.
About sessions, about something in the… in the spansum, and… Unlock records, but… It's not as efficient as we would want to.
So, repeating, repeating information across all spans and logs, on the SDK browser is… It's kind of lame.
Just to say it plain, and in plain English. So, I would prefer to do something. So, the entities kind of wants to, or at least the spec wants to have some… something in resource, which is… The, identifying attributes, something that is static, which is part of the resource, and then you have the entities, and… You have these descriptive attributes, which belongs to the entities, but the implementation is something that, yeah.
It's weird.
**Trent Mick** 08:42 Okay.
**David Luna Bistuer** 08:43 It doesn't win.
**Trent Mick** 08:44 Okay. That's the part where I feel I'm missing, and that's an important part to get before having an opinion, because I'd read the spec a while back when it was… Talking about identifying attributes and non-identifying attributes, but… It wasn't and still isn't clear to me what lands in… the OTLP data that gets sent, and whether the protobuf is changing, and some discussion on some…
**David Luna Bistuer** 09:08 like.
**Trent Mick** 09:09 initiatives being discussed last week. I saw someone said, like, maybe this isn't a breaking change, because it's not changing what gets sent through OTLP, and I'm like, well, so I don't know, understand.
**David Luna Bistuer** 09:18 If we go that path about the defying attributes and entity attributes, the protocol changes, so we add more information on the resource. And also, it's something that we don't know, so we don't know how the backends are going to process that, so… Usually, there is… there might be the use case that some backends actually get all the attributes from a resource and treat them, treat them as identifier attributes, so they use the… whole set of attributes to identify your research.
So now if the telemetry from the clients are sending more attributes that are changing over time, these backends are going to interpret them as different attributes, like… as different resources, sorry.
Yep. So, they might misinterpret what the… misinterpret the implementation that they are ingesting. So that's our concern.
In that sense.
Right. So, well, if we're… I'll let you know in the upcoming, Meetings, if we are doing some advance, or I will paste here any link, or… PRs or conversations and discussions about this.
**Trent Mick** 10:32 Okay, yeah, definitely. So I guess, I mean, this is a heads up right now, but, Yeah, if you're able to rope in Dan at some point.
I'm sure Dan's gonna notice it, too. But yeah.
**David Luna Bistuer** 10:43 Okay.
Thank you.
**Trent Mick** 10:48 Great. Aaron?
**Aaron Abbott** 10:52 Hey.
**Trent Mick** 10:55 Hi.
**Aaron Abbott** 10:55 Looks like I'm… oh, there we go. Hey, Trent, I didn't know… I didn't know if the dot dot dot meant to go above the line there, or were you… did you want to go first?
**Trent Mick** 11:04 Oh, that was me, because I was throwing stuff towards the end, the meeting, so that's perfect, yeah.
So this is me, AB, yeah.
**Aaron Abbott** 11:13 Cool.
**Trent Mick** 11:15 Let's go ahead, yeah.
**Aaron Abbott** 11:16 Yeah, yeah, I just wanted to say hi. I'm from the… mostly from the Gen AI SIG, and I think Trent and Jamie, we've seen you in the Gen AI SIG as well.
So for folks who don't know, we did, Open Inference was donated to OpenTelemetry, which is basically like an intro of third-party instrumentations, including JS and mostly Python.
And we're kind of slowly breaking it into instrumentations in this new repo, which I can leave a link to.
**Trent Mick** 11:46 That's OpenAI, Jenny.
Eye Instrumentations, I think.
Okay.
**Aaron Abbott** 11:54 It's like this. And I think we've discussed this, Jamie and Trent, like, I guess the first question is, is there any interest in porting over some of those open inference donated instrumentations that were written in JavaScript To the JS SIG, and would you want to do, like, a separate repo? Would you want to do contribib?
I just kind of wanted to get the ball rolling. And actually, my coworker was gonna discuss this, but he got… He's having some trouble with, like, transportation, so he had something he might present next week, but I just wanted to get a pulse.
**Trent Mick** 12:31 I, like, I want to jump out and say, yeah, for sure, but I know that we've had problems maintaining a lot of instrumentations in the Katrib repo, so, the main thing is whether there are Gonna be code owners for… For those maintaining them, and, like, sometimes you get… Yeah, I don't know. Do you know if there are… Yeah, I don't know.
Do you know if there are likely people that would be willing to drive most of that work? Like, certainly maintainers can help on dealing with the process on… The contribib side and getting, reasonable reviews, though not necessarily, like, reviews from people who have expertise in a particular package.
**Aaron Abbott** 13:24 Yeah, I mean, I can… I can also advertise this. I know this has been an issue with… I think there's already one for LingChain.js in Contrib, and I know this has kind of been an issue, but… I can also, you know, check with folks in the Gen AI SIG, see what they think, and I don't want to speak for my coworker, but we could probably offer to be code owners on some of them.
**Jamie Danielson** 13:46 That's what I think, similarly for us, I've slightly switched roles a little bit for the quarter, so… I… but I do have another coworker who is trying to help out with the instrumentations, too, so we can try to, like.
be code owners on that as well. I'm super interested in it, I think it's useful. And I think generally, we've talked previously in the SIG about those new instrumentations, we just kind of knew, like.
it's beneficial that it's coming from a place of people who did know what they were doing at the time, so it's not, like, starting from scratch, which is useful. And I think either way, we probably have to get them in at some point.
So, I think that's just the main thing, is the effort to update them and get them in.
Because the other thing, right, we talked about was, because we still don't have a way with our auto-instrumentations node package to bring in third-party instrumentations, if someone were instrumenting that way, if we want people to be able to use it, it has to be in our JSontrib repo today, unless we prioritize the changing of our node,
**Trent Mick** 14:53 We want them to use it in certain scenarios. So, like.
**Jamie Danielson** 14:55 Correct.
**Trent Mick** 14:56 Having to have a dependency other than that, or the way… Like, the operator… hotel operator is wired up, then…
**Jamie Danielson** 15:04 Right, like the zero code.
**Trent Mick** 15:06 Right.
**Jamie Danielson** 15:07 like, the zero code instrumentation path, it has to be in JSContrib. If they are instrumenting, or at least doing, you know, setup.
With code, then it's not a big deal at all.
**Trent Mick** 15:18 Yeah.
Yeah.
Which is kind of the wrong driver for these things, so it should be other… other things that are deciding that. But, like, Jamie, if you are… is that Mike that you're talking about? Your core?
Or is that someone else that…
**Jamie Danielson** 15:30 Mike and I are both kind of doing something a little bit different, but also, like, obviously, Eng is still interested. Wolfgang is the other person, he works in, like, browser SIG and has been to a few Gen AI things as well. So I can bring this back.
**Trent Mick** 15:45 It sounds like, for sure, if Wolfgang and you said someone, Aaron, that you knew are willing to be code owners on some to get started, at least? Like, I don't know, I assume it's easier to start with one, and then get a feel for it, and then decide on others going forward. How many instrumentations are we talking about from… Open inference, do you know? Offhand?
**Aaron Abbott** 16:04 Yeah, yeah, it's… it's on the order of, like, 10. It's not a ton, and I don't think that we need… like, we can look at NPM download stats and figure out which ones are most important. Like, obviously we have our opinion of which ones are important, and You know, it doesn't have to be all or nothing.
And, Yeah, yeah, so I think you all know Pranov, he's my coworker, he joined a couple of SIGs, he was doing the work on, like, batching and the JS metrics, for example, so… I mean, I'll let him know that there's… there's good interest here, and maybe he could… he has, like, a doc with some of this information, maybe he can share it next week. It sounds like there's general interest, but the main concern is just code owners.
**Trent Mick** 16:44 Yeah, always. There's so many instrumentations in there, and a lot of them are listed as unmaintained, so sometimes that can end up being a burden. Yeah, so that said, I think it would be… this would be great.
Then, so… One of the caveat is I'd be interested, of course, in Mark's opinion. He's kind of one of the more active maintainers. He's just away for 2 weeks now, so… We'll… we'll see and get an opinion on that. The… so, some background on the other one. So, we have an OpenAI instrumentation there, I'm not sure it's getting a lot of love. We have, a… template, or the start of the line chain one. So that instrumentation line chain that you saw right now is not currently being published. It was… my understanding is it was going to be a couple of stages, so just getting in the… The structure, and then… The main code was going to be added before… It actually gets published, so… I don't actually know what the current state of that one is.
If that matters.
Okay.
Would there be naming collisions in these, or I haven't looked at… I don't know the open inference ones at all.
**Aaron Abbott** 17:51 Yeah, so they use scoped MPM packages, which I think we do as well in JS, so… I don't think there's naming collisions, but there were some questions there, because we're kind of branding the Python ones as, like, OTEL GenAI.
Because what we're seeing a lot of other companies have done is they have, like, a distro of instrumentations, they call it, like, open inference or open nullometry, so there is probably some naming question, but I don't think, collisions should be an issue.
**Jamie Danielson** 18:22 I'm trying to remember where… there was conversation about naming somewhere, and I'm having so much trouble finding the issues or whatever.
related to this, where some of the conversations happened. I just posted.
**Trent Mick** 18:36 Sit in, like, the gor.
**Jamie Danielson** 18:38 Doc.
**Trent Mick** 18:39 Okay.
Yeah, some of that I thought mostly was from Python, when OpenLelementary was…
**Aaron Abbott** 18:45 Yeah.
**Trent Mick** 18:45 in the process of donating some stuff, they… because they weren't… like, so MPM, we have at OpenTelemetry, and no one else can publish to that, so there's… It… but in Python land, at least until in the last couple of months. Anyone can publish with any name, and using OpenTelemetry- as a prefix.
wasn't… actually explicitly discouraged, but I think now it's impossible, right?
**Jamie Danielson** 19:09 I don't think it's a massive one of…
**Trent Mick** 19:11 We know, so PyPi added a thing so that there are, I think.
three namespaces right now that are guarded, and OpenTelemetry is one of them. I thought, or I can't remember if the OpenTelemetry was an exception, because there are already pre-existing cases or whatever, so it's a bit of a mixed bag in Python Lab, but…
**Aaron Abbott** 19:29 I'll catch up on that, because I know that there was a pep for it, and I talked with the author, like, a Python enhancement proposal for fixing this in PyPy, and… I don't know if it was ever… like, last I looked a couple months ago, the discussion had kind of died, but I'll check, which is helpful, but yeah, like, I think in JS, we're fine because of the scope packages.
**Trent Mick** 19:49 Yeah. Yeah, agreed.
Yeah, so there's this… I'm not sure what the status is.
**Jamie Danielson** 19:58 Oh yeah, so that doc I put in there, too, has, at least whenever this was done, whenever this was written, includes downloads last month.
Which may be helpful as a starting point.
That one, yeah.
So this has, like, everything, including Python, but if you scroll down, there's, like, a JS section, with, like, a table.
Yeah.
**Trent Mick** 20:28 So… I mean, this is stuff to be sorted out, but so, like, are we talking about having an… at OpenTelemetry slash Instrumentation MCP?
**Jamie Danielson** 20:39 I think so, yes.
**Trent Mick** 20:41 Okay, so the naming collision, then, that I meant is this one. If we already have an instrumentation OpenAI, what.
**Jamie Danielson** 20:46 Alright…
**Trent Mick** 20:48 Do we want to look at merging the two, or deciding which one's better, and doing a swap over, or something like that?
**Jamie Danielson** 20:55 Yeah, it's okay.
Oh, go ahead.
**Aaron Abbott** 20:57 Oh, Jamie, please, if you… I think you've been in the SIG, you know what the… what the scoop is.
**Jamie Danielson** 21:02 Yeah, like, the general idea is the instrumentations that were donated need to be updated to be more, like, up to spec with OTEL, including, you know, updated GenAI semantic conventions and things like that.
So if there's any that we do have, which again, might just be the Lang chain and the OpenAI one, the idea, I think, would just be, yeah, what can we take from this instrumentation that we don't already have and update our own, as opposed to needing another brand new instrumentation, just kind of like… like you said, merging the two, taking what's good from both, and… updating ours.
**Trent Mick** 21:35 Yeah, I definitely think for a user's point of view, you only want one. Having two is kind of crazy, so…
**Jamie Danielson** 21:40 Necessary.
**Trent Mick** 21:40 Give me some work on deciding and looking at what's better there. And then, is there eyes… Is their intent, then, to… eventually point theirs towards the OpenTelemetry ones and say, hey, people use those.
**Jamie Danielson** 21:54 They said they're still maintaining theirs, this is just to help us get a head start in OpenTelemetry, because I think Dan asked that question on the… donation issue itself.
**Trent Mick** 22:06 Okay.
Okay, so there's some reading.
**Jamie Danielson** 22:08 Yeah, here's a… here's a link I just put in chat, but I can put in the… other thing, too.
**Aaron Abbott** 22:19 Yeah, I think that's…
**Jamie Danielson** 22:20 So, if there's anything new there?
**Aaron Abbott** 22:22 No, no, not really. This was kind of like a one-time donation, was the way we phrased it. It was kind of like to see OTEL with some more instrumentations, and we can revisit with them, you know, in a couple months or whatever. So, you know, we… I think someone from Arise usually joins the Python SIG and, But yeah, there's no intention right now to merge them.
**Trent Mick** 22:49 And there's a weekly Gen AI SIG, right? Is that where… this is kind of the owning SIG for this work, then it would be.
**Aaron Abbott** 22:56 Yes, yeah, so we do semantic conventions, and we do instrumentation discussions, which is obviously most of it in Python at this point. It's Tuesdays at, you know, if anyone's welcome to join, it's Tuesdays at noon Eastern time.
**Trent Mick** 23:11 Okay.
**Jamie Danielson** 23:12 Yeah, like, it used to just be SEMCOMF, and I think there was another meeting on Mondays, but it was lightly attended on Mondays, so it just got combined to best of everything.
**Trent Mick** 23:22 Are you on that regularly, Chimney?
**Jamie Danielson** 23:24 Yeah, I have been kind of hit or miss lately, because, like, mostly right now I'm, like, working with, like, solution architects based on Honeycomb, so I'm, like, less in the end side, but we do still have a team, like, actively working through LLM observability, so I've been trying to attend when I can.
**Trent Mick** 23:39 Because the crossover would be great, basically, if we had it by accident, yeah.
**Jamie Danielson** 23:43 Yeah.
**Trent Mick** 23:44 Okay, cool. So, yeah, Aaron definitely has an interest, and if… Bernal, if I had his name right, was… going to present sometime, that would be great, too. Yeah.
**Aaron Abbott** 23:57 Okay, cool. Yeah, maybe, I think he could probably make it next week, and he also has a doc, maybe we'll share it out, like, on Slack, and it has some of these details in it, but… Yeah, sounds great, thank you all so much. Appreciate it.
**Trent Mick** 24:10 Great, thank you.
**Jamie Danielson** 24:11 Thanks, Erin.
**Trent Mick** 24:14 Right.
**Abhinav Mathur** 24:15 This one, Dylan already asked me, so they're good.
this one. I just… I was just looking to, take this over, but, He already assigned it to me, so we're good. That was not on the item.
**Trent Mick** 24:28 Oh, I see. Okay, cool. This is… Okay, Ivan, I saw this issue, I haven't read what the details are, what the answer is, but… Okay, you're gonna take a stab at it?
Basically, it's great.
**Abhinav Mathur** 24:44 Yep, go ahead.
**Trent Mick** 24:46 David and I, I think, are listed as the instrumentation and DT maintainers, so… Definitely hit us up if you have questions.
**Abhinav Mathur** 24:57 Will do. Thank you.
**Trent Mick** 24:59 Yeah, cool.
Okay, please… If anyone has other topics, bring them up. But, I wanted to ask questions about a couple P1s that I saw.
So, and contrib… David, are you still around?
**David Luna Bistuer** 25:22 Not… hmm… It should be a PR.
**Trent Mick** 25:27 So there it is. Yeah, there was a PR for this one.
Had you taken a look at this yet, or no? And… I guess the PR only came in yesterday, so… no.
There you go.
Okay, so I guess we wanna… you've had some discussion with…
**David Luna Bistuer** 25:44 Yeah, yeah, yeah.
And after the discussion, and then this,
**Trent Mick** 25:48 Oh, cool.
**David Luna Bistuer** 25:56 So, yeah, I'm going to finish today on reviewing it, but it's… I think it's good to go.
So, long story short…
**Trent Mick** 26:03 You already started looking, thinking.
**David Luna Bistuer** 26:04 Yeah, so long story short, I need to review the tests, but long story short is that You can use a Devon Listener without Directly, without calling the element, so then the Ds.
keyword becomes, reference to the undefined, and this is not accepted by the WIC map. So… and oddly enough, Web Vitals instrumentation is using that specific series, it's using the Add Evolution API without, any, any context.
Directly.
So, it's kind of a quirk from the browser.
Okay, so this, this adds a safeguard about this, so whenever whoever is calling a demo listener, we check if this reference is valid or not.
Before, keeping track of it.
So, yeah.
**Trent Mick** 26:59 Okay, cool. So, if we got… I mean, I guess… That's some thumbs up, so some people are being impacted by this, so we should probably get.
**David Luna Bistuer** 27:11 Truly so.
**Trent Mick** 27:12 Fairly soon after we get this. Okay, cool.
There's some older ones that have been sitting around for a while.
This one's not too old, I guess. I didn't notice this one.
This one's assigned to you. Had you intended to take a look at this one? Paco's also…
**David Luna Bistuer** 27:36 Unlimited.
**Trent Mick** 27:37 commenting on this.
I'll go back up to the top.
**David Luna Bistuer** 27:48 Why is it so fun to me?
Okay, interesting.
How did that get assigned?
**Trent Mick** 27:55 He assigned on July 1st. Did we have a meeting on July 1st?
**David Luna Bistuer** 28:01 Okay…
**Jamie Danielson** 28:02 Surely David wants this one.
**David Luna Bistuer** 28:07 Okay. I also review all the donations from Digene AI, don't worry. You got it. One thing I would suggest.
**Jamie Danielson** 28:15 I would suggest asking if they could move the repro into a GitHub repo, because I don't know if you all remember, there's been some,
**David Luna Bistuer** 28:24 Chanel.
**Jamie Danielson** 28:25 Shenigans where people are putting bad stuff into issues like this?
**Trent Mick** 28:29 Fireballs?
**Jamie Danielson** 28:30 Yeah.
but bad stuff in that tarball. It's not like, oh, here's your nice repo, it's like, here's your nice repo, I'm taking over your computer kind of thing.
General.
the internet.
**Trent Mick** 28:41 Oh, yeah, for sure. David, also, if you don't have bandwidth, you can take your name off this. You're not required to…
**David Luna Bistuer** 28:46 Okay.
**Trent Mick** 28:47 this one.
And let me If so, if so, I'm willing to take a look, too.
**Jamie Danielson** 28:52 Oh, probably because it says Ndichi in the… Stacked there, in the error.
**David Luna Bistuer** 28:59 Okay.
**Jamie Danielson** 29:00 That's why.
**Trent Mick** 29:03 Yeah, but that's just because.
**Jamie Danielson** 29:04 I know, I don't know if that's a…
**Trent Mick** 29:06 She, underneath.
**Jamie Danielson** 29:06 You're in charge of all, indeed.
**David Luna Bistuer** 29:08 Has the HTTP.
**Trent Mick** 29:09 Key client is your fault. No, yeah.
Okay.
Yeah.
It is probably because you opened your mouth on July 1st. Okay.
And then there are older ones… which I haven't taken a look at. This… I thought we'd gotten over this hump, but maybe we didn't go back and close this issue.
Because we did do updates for the Smithy Core.
**David Luna Bistuer** 29:35 Yeah.
**Trent Mick** 29:36 Unless it's another one that's happened, but this is the one I remember from late last year.
Okay, so I'll… I'll come back and take a look and see if this one can get closed. Flaky tasks, I'm not… I'm not sure.
And then… I don't want to go back to 2023 right now, thinking… And then… query repo… This one is quite recent.
Sorry, just jumping around first and holy right up, Batman.
Okay, Mark said he would take a look, and there is a PR for it.
on.
And Matt took a look.
Okay.
If someone wants to, they're more than welcome, otherwise I'll take a look later today, this one.
And then I think if we get those 2 or 3 in, then I can start doing a release.
At this point, it won't get done before Friday, so probably next week, I'd start taking a look on Monday.
But doing a release set.
Fashion-related tape error.
Who added the P1?
Oh, this is unbund. Okay.
Anyone using bun much?
Okay.
Yeah, I agree.
And I'll raise your hands at the same time.
Do we actually have a… oh, we do have a runtime fun there. Okay, good.
It was early last year.
I'll stop at this one, if anyone's getting itchy to get out of here, because this gets crazy.
Dan had been assigned because he's the time man.
Okay, I'm gonna take a quick look after, and maybe bug Dan to see if he has bandwidth again for that, but… I don't use Cloud for our workers myself, so… Can't help.
Okay… it's half hour past, and there's some other SIG Meetings that are only half an hour that are kind of wonderful. So… unless anyone wants to make a case for it, I'm gonna skip doing triage this week.
We'll come back next week when Jamie's running the show.
We can do it then.
**Jamie Danielson** 33:06 Works for me.
**Trent Mick** 33:07 Okay, if not, thank you all.
Emma.
**Abhinav Mathur** 33:10 Thank you.
**Jamie Danielson** 33:11 Happy Wednesday.
**Trent Mick** 33:12 See you next week.
**David Luna Bistuer** 33:14 Me too. Bye.
