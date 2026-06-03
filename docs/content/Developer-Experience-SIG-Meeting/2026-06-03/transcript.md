SIG: Developer Experience SIG Meeting
Date: 2026-06-03
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Johanna Öjeling** 01:15 Hey, Pirate!
**Perk (Marcin Stożek) | Elastic Ingest** 01:17 Hey, Ana, how are you?
**Johanna Öjeling** 01:18 I'm good, thanks. How are you doing?
**Perk (Marcin Stożek) | Elastic Ingest** 01:21 I'm good, yeah, very well.
when… When is the time that you move?
**Johanna Öjeling** 01:28 So, Friday is my last day working at Grafana, and then I take PTO, for the rest of June, and I start the new job on the 1st of July. Oh, nice. Yeah, so right now I'm looking forward to, yeah, taking some PTO and, completely switching off.
**Perk (Marcin Stożek) | Elastic Ingest** 01:49 Workplace.
**Johanna Öjeling** 01:50 Oh, that, yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 01:51 Oh, very well, okay. Enjoy.
**Johanna Öjeling** 01:53 Yeah, thank you.
**Perk (Marcin Stożek) | Elastic Ingest** 01:54 You should do it. Yeah.
**Johanna Öjeling** 01:57 Do you have any, plans for the summer? Any upcoming… Perk (Marcin Stożek) | Elastic Ingest 02:00 So we're just going, you know, like, with, with the family and friends, or, and kids, the lake, and then just, you know, like, small travels here and there.
**Johanna Öjeling** 02:12 Mmm, see, nice.
**Perk (Marcin Stożek) | Elastic Ingest** 02:14 Not, like, a month long.
Okay.
**Johanna Öjeling** 02:16 Where do you live? I forgot.
**Perk (Marcin Stożek) | Elastic Ingest** 02:19 Poland.
**Johanna Öjeling** 02:20 In Poland, okay.
**Perk (Marcin Stożek) | Elastic Ingest** 02:21 Yeah, so, I'll stay.
**Johanna Öjeling** 02:23 Which part docodeLab?
**Perk (Marcin Stożek) | Elastic Ingest** 02:24 Oh, actually at the, near the German border, very close to Berlin.
**Johanna Öjeling** 02:28 Okay. You?
in Sweden, near the border to Denmark.
**Perk (Marcin Stożek) | Elastic Ingest** 02:34 Okay.
**Johanna Öjeling** 02:35 Sweden, yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 02:37 I'll give him a.
**Johanna Öjeling** 02:38 Juliana?
**Perk (Marcin Stożek) | Elastic Ingest** 02:39 Hey, Julian So, Juliano, where are you based? Tell us.
**Juliano Costa | Datadog** 02:43 I'm based in Austria, it's Linz, which is… Perk (Marcin Stożek) | Elastic Ingest 02:48 Okay.
**Juliano Costa | Datadog** 02:49 Close to, well… close to Munich and Prague, so I'm, like, here.
I'm between Munich and Vienna, so, like, let me know.
**Perk (Marcin Stożek) | Elastic Ingest** 03:00 Okay, okay, okay.
**Johanna Öjeling** 03:02 We all live close to the border, to a different country.
**Perk (Marcin Stożek) | Elastic Ingest** 03:06 Yes, yes, yes, yes, yes, that's how it is.
And then, for me, it's like, you know, whenever I fly, I fly out from Berlin, for example, because it's best.
Yeah, it's closer, actually, closest.
**Johanna Öjeling** 03:17 - yeah, same here, I always fly from Copenhagen.
**Perk (Marcin Stożek) | Elastic Ingest** 03:21 Yeah, you're saying? Yeah. Okay.
Telecare.
**Juliano Costa | Datadog** 03:26 about that, did you submit, did you… any of you submit anything to the events happening? So there is cloud-native Cloud Native Denmark. I think the CFP is still open.
And there was cloud-native Poland that the CFP was closed, two days ago.
**Johanna Öjeling** 03:47 Yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 03:48 I've sent for also.
**Juliano Costa | Datadog** 03:53 So, you, you sent to… Perk (Marcin Stożek) | Elastic Ingest 03:55 Apoge one.
**Juliano Costa | Datadog** 03:55 Morrisall? Yeah, -h.
**Perk (Marcin Stożek) | Elastic Ingest** 03:56 Cool.
**Johanna Öjeling** 03:58 Yeah, I haven't submitted to, any, but yeah, I wonder, do you know, is the cloud-native Denmark taking place in Copenhagen, or… or who's?
**Juliano Costa | Datadog** 04:10 I…
**Johanna Öjeling** 04:11 Or maybe elsewhere.
**Juliano Costa | Datadog** 04:12 It's not our host this year, our host was, last year.
**Johanna Öjeling** 04:19 Okay, okay.
Yeah, I would like to go to some conference in Denmark, actually.
Okay, yeah, or her slab. Probably Copenhagen this year. Okay, if it's still open, maybe I'll do a last-minute submission. Did you submit to anything, did you know?
**Juliano Costa | Datadog** 04:39 For… Barcel, yes, and for… Denmark, I think so? Let me open my session eyes.
I think, I think I already did.
**Perk (Marcin Stożek) | Elastic Ingest** 04:55 Very well. I'll be in Warsaw regardless.
So…
**Juliano Costa | Datadog** 04:58 Denmark, Yes.
**Perk (Marcin Stożek) | Elastic Ingest** 05:00 Oh, very well, very well. Cool.
**Juliano Costa | Datadog** 05:02 Cool, yeah, for Versa, I would only go if I get a topic.
**Perk (Marcin Stożek) | Elastic Ingest** 05:06 Oh, yeah, hopefully.
**Juliano Costa | Datadog** 05:07 Hopefully that will happen. Yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 05:10 Sometimes…
**Juliano Costa | Datadog** 05:11 But, yeah.
The one in Varsal, I already gave this feedback to the team. It was the… the conference with more observability talks that I… that I've seen, like, it was a one day, and it had, like.
**Perk (Marcin Stożek) | Elastic Ingest** 05:29 Wasn't it, exactly?
**Juliano Costa | Datadog** 05:31 Yeah, it was really good, like, all the contributors and maintainers there, I was like.
**Perk (Marcin Stożek) | Elastic Ingest** 05:36 That wasn't.
**Juliano Costa | Datadog** 05:36 impressed.
**Perk (Marcin Stożek) | Elastic Ingest** 05:37 Yeah, yeah. So, you were there, because I was there as well.
Last year.
**Juliano Costa | Datadog** 05:42 Yeah, I think I first met, first met there, I first met you there.
You were with.
**Perk (Marcin Stożek) | Elastic Ingest** 05:49 Andrea McCoy.
**Juliano Costa | Datadog** 05:50 Yeah, we collect, yeah, Perk (Marcin Stożek) | Elastic Ingest 05:53 Oh, maybe. Oh, okay, okay, okay, okay, very well. Hopefully we'll see each other again.
**Juliano Costa | Datadog** 05:59 Gave the… it smells like clean telemetry talk there. My Nirvana-based talk.
**Perk (Marcin Stożek) | Elastic Ingest** 06:05 So everyone.
Did you stand for the… for… because for KubeCon as well, KubeCon is closed, and then the observability Day is open, still.
**Juliano Costa | Datadog** 06:13 Yeah, I submitted a couple of things there as well, With some colleagues. So, yeah, let's see.
**Perk (Marcin Stożek) | Elastic Ingest** 06:22 Better go.
**Juliano Costa | Datadog** 06:23 let goes. KubeCon is tricky, so… Perk (Marcin Stożek) | Elastic Ingest 06:26 Oh, it is, it is, it is, isn't it? It's a very… you know, whenever I think about it, I think it's for good reason. It feels like, Maintainer-led?
conference? I mean, a lot of talks are given by the maintainers, and then for people that are actually, you know, doing the software, and it feels very well, it's not like… you know, sponsor-driven talks and whatnot, not vendor-driven talks. It's, you know, about the community for the community. It feels great, really.
**Juliano Costa | Datadog** 07:01 Yeah, yeah, I love that, yes.
**Perk (Marcin Stożek) | Elastic Ingest** 07:06 Especially when you compare it to other conferences. I don't know whether they try to do this or not, but this feels very well for me.
**Juliano Costa | Datadog** 07:16 Yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 07:20 Okay, what do we have on the agenda?
**Juliano Costa | Datadog** 07:22 I'm creating it, right now.
**Perk (Marcin Stożek) | Elastic Ingest** 07:27 Oh, huh.
**Johanna Öjeling** 07:27 They're welcome.
**Juliano Costa | Datadog** 07:31 See?
Okay… So, you are already on… IKEA.
Johanna.
**Johanna Öjeling** 07:45 No, I'm starting on the first dog.
**Juliano Costa | Datadog** 07:47 July, July, July, okay.
**Johanna Öjeling** 07:49 So I'm still at Grafana, this week, and then I take PTO for the… yeah, so Friday will be my last working day here, and then, three and a half weeks of vacation, for stopping the new job.
**Juliano Costa | Datadog** 08:05 Cool.
Good luck, and I hope, I hope… to continue to see you,
**Johanna Öjeling** 08:11 Yeah, thank you.
Okay.
**Juliano Costa | Datadog** 08:18 So…
**Johanna Öjeling** 08:18 to still, stay connected to the open source space and hotel, community. So, I, yeah, I will continue to, attend the meetings, as far as is possible.
**Juliano Costa | Datadog** 08:34 Awesome, yeah. I like working on the open source community, because sometimes you'll switch companies, but you still continue working with the same folks, so…
**Johanna Öjeling** 08:44 Exactly, it's like now when I say goodbye to my coworkers at Grafana, they're like, okay, let's see you in, like, CNCF Slack, or yeah, at open events, or yeah, so that's… that's quite nice.
**Juliano Costa | Datadog** 08:58 He did.
Da-da-da… let me see… What do we have here? So I just created the tab for the telemetry level proposal.
But I haven't started writing it.
I… I do have a draft local… locally.
But I'm still refining, refining it. I want to add some context on wide, why the… the config file, the… what's it called? The declarative config?
Doesn't solve that.
And why a telemetry-level environment variable or configuration would be a better approach for end users, because in our case, we are the developer experience Seek, so we try to Have a better… developer experience.
And… for the developer, I don't think he needs to actually care about, wh-which… Libraries, he should instrument, or not.
At least at the beginning. Maybe that's something like today, day 3 or day 4.
But DayZero, they want to… I don't know, install the auto instrumentation and let it go?
But… Ideally, we as hotel, we just… the default should be something like less variables.
with, I don't know, boundaries and, like, Maybe client-server, producer-consumer.
But we drop from the default internal, and we drop, middleware spins.
From the default behavior, and if the user then wants to see more stuff, then he switches or enable that telemetry level to verbals, or some other term that we agree, and then that produces more like, all the middleware, all the internal spins and everything, then you get, like, more context. But… the problem for me, and that's one of the reasons why I actually raised this, thing, is that we produce a lot of telemetry by default.
And not all this telemetry is useful.
For most of the users, even during troubleshooting.
So, yeah, that's what I wanted to say here on this telemetry-level part.
**Perk (Marcin Stożek) | Elastic Ingest** 11:50 Definitely. You know, like, when you, when you have it written down, just, you know, please ping us, because I'm definitely interested.
That's like, I see this, I see this for a long time as well.
**Johanna Öjeling** 12:05 Yeah, just, let us know when you have, ported it over to the doc. It'll be interesting to have a read.
**Juliano Costa | Datadog** 12:14 Whoa.
And I see that the documentation, changed. I, I, I checked last, yesterday. It wasn't like that, was it?
**Johanna Öjeling** 12:24 No, exactly. I also write it, like, in private doc, and then I copy it over, but now, like, okay, I will, I need to put, like, yeah, since I will lose access to my, like, rough on my accountant, right, I will… I need to carry everything over. But yeah, I… I also need to refine it a bit more, but I still put, like, rough draft, so please have a read, when you have the possibility. And also, Juliano, let me know if… if this was kind of the idea you had, or, yeah, if You had something else in mind.
**Juliano Costa | Datadog** 13:08 Okay.
I want to… I just want to find… document that I… Not a document, but, a page that I found yesterday.
while I was navigating… Finder… declarative.
Give me just a second. I want to share a couple of stuff But one thing that I… that I found on the docs, that… That could be valuable for us?
But I… I don't know where… where was that? Maybe I can find on my history?
There you go, awesome.
I'm gonna share… I'm gonna put on the Google Docs.
**Perk (Marcin Stożek) | Elastic Ingest** 14:50 Okay.
**Juliano Costa | Datadog** 14:51 Actually, on YardDock, I don't know where.
maybe in goals, I'll just add, idea… No, I'm gonna share my screen.
Give me some… Can you see the configuration types reference? So this is something that is under the configuration docs, under the spec.
And I'm pretty sure this is coming from somewhere automatically. So, like, they are not updating that manually.
And… Even though the page is a bit, cut, get some love.
could receive some love. I still think this is super valuable, because, like, you can search for components, like the batch, for instance, and then you'll get all the batch processors in that case.
And, when you click on the drop-down, then you have all the… other properties that this processor accepts.
So this is super cool, actually, because… this… this solves one of the pain points that I have, for instance, whenever configuring a component. Sometimes I want to configure, or I'm not even… I'm not even aware of, the component… the… options that I can configure and enable within the component, and then I need to go to the GitHub, and sometimes the example that they have there is not a full example, so then you need to go to the Go code and, like.
find out what you need to do. And this is super helpful, because then it simply explains, so the batch spend processor has scheduled delay, export timeout, next queue size, whatever, and it has, like, a description, a type.
And, yeah, this is super cool. I think this is coming from somewhere.
So, maybe we could, View the page source, and, kind of… investigate how this is actually created. So, like.
**Johanna Öjeling** 17:35 Hmm.
**Juliano Costa | Datadog** 17:36 This is coming from this, config types accordion. Because, basically, that's the idea, right? We have… Something that is being created dynamically, And if we can have… If we can have this script.
patching the data directly. I don't know if that's how it is done, today on the… on the docs. But if this accordion thingy alias here is actually fetching directly from the collector, then we solve the problem. Like, we just need to… we just, here, with a lot of quotes.
need to kind of advocate that to all other SIGs, so then they can always follow the same pattern. And then we have, on the docs, we have, Some sort of import that will just work and be up to date with whatever they have on the repos. So now maintainers do not need to maintain their repos and docs, they just need to maintain their repos, and that is… Way easier to handle than all this cross… Report things.
**Johanna Öjeling** 18:52 Yeah.
Cool, yeah, thank you for sharing. I wasn't aware that… aware of these configuration types, but it's really useful, and yeah, I'll look into if I can find how that is rendered.
**Juliano Costa | Datadog** 19:07 Yeah, I wasn't aware as well, yeah.
**Johanna Öjeling** 19:08 Yeah, if it's… I wonder, yeah, if it works in a similar way as the spec'd pages, or if this uses a different approach.
**Juliano Costa | Datadog** 19:17 No.
**Johanna Öjeling** 19:18 But yeah, thank you, Liam.
**Juliano Costa | Datadog** 19:24 Yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 19:25 do I assume correctly that this is, function of the engine that creates the webpage, this accordion that is shown.
**Juliano Costa | Datadog** 19:33 Let me… let me find… so… Perk (Marcin Stożek) | Elastic Ingest 19:35 y'all, maybe?
**Juliano Costa | Datadog** 19:36 In the hotel.io, we use Yugo.
So let me find the definition of that.
So, this is a short code.
**Perk (Marcin Stożek) | Elastic Ingest** 19:52 Because I wonder… I wonder…
**Juliano Costa | Datadog** 19:53 share my screen.
**Perk (Marcin Stożek) | Elastic Ingest** 19:54 How does it… how does it look from the other side?
**Juliano Costa | Datadog** 19:59 So this is the… disrupt.
**Perk (Marcin Stożek) | Elastic Ingest** 20:02 coded for…
**Juliano Costa | Datadog** 20:03 For this accordion, so then this is fetching, from… JS config types accordingly.
So, I don't think this is… what I dreamed of.
Because then I think someone needs to keep this up-to-date.
Let me just see where the… Or is this JS holder?
Am I blind?
Maybe it's data?
**Perk (Marcin Stożek) | Elastic Ingest** 20:38 Maybe you can go to File, there's go to File up there, and just start typing the config type accordingjs.
Oh.
**Juliano Costa | Datadog** 20:49 Thank you.
**So, that's interesting, because here it says… Perk (Marcin Stożek) | Elastic Ingest** 20:54 I think it's the first one.
**Juliano Costa | Datadog** 20:55 field.
**Perk (Marcin Stożek) | Elastic Ingest** 20:56 Is the first one.
Oh, no.
**Juliano Costa | Datadog** 20:59 Okay, wait, yeah, here it is, yeah, yeah.
**assets… Perk (Marcin Stożek) | Elastic Ingest** 21:03 Classic.
**Juliano Costa | Datadog** 21:04 JS. Okay.
**Perk (Marcin Stożek) | Elastic Ingest** 21:04 Yeah, that makes sense.
**Juliano Costa | Datadog** 21:06 And then… okay, so actually this… As a whole, like.
Yeah, the whole JavaScript for expanding and all the values and stuff.
Or… wait, or not. We don't have all components here.
**Perk (Marcin Stożek) | Elastic Ingest** 21:29 Yeah, so where does the doctor come from?
**Juliano Costa | Datadog** 21:30 So, this is cool. Okay, so… it's com… Perk (Marcin Stożek) | Elastic Ingest 21:36 Let's go deeper.
**Juliano Costa | Datadog** 21:37 Yup.
I… I'll just point Claude here and say, hey, Explain.
**Perk (Marcin Stożek) | Elastic Ingest** 21:47 Yeah, yeah, yeah, yeah, yeah. Definitely.
**Juliano Costa | Datadog** 21:52 But I… I mean, this is promising, so… As long as we do not need to have… Perk (Marcin Stożek) | Elastic Ingest 22:02 Excellent.
**Juliano Costa | Datadog** 22:03 all the values and everything that we want in a new file in the docs, and this is coming directly from the upstream repo, then this is perfect. This is exactly what what we are discussing here, so… Yep.
**Perk (Marcin Stożek) | Elastic Ingest** 22:19 Agreed, agreed, yeah.
Very nice.
**Juliano Costa | Datadog** 22:24 Johanna, do you know Jay DeLuca? I think he's Grafana, right?
**Johanna Öjeling** 22:31 Yes.
**Juliano Costa | Datadog** 22:32 He… he was the one, So that's why we didn't know about this page. This was published 3 weeks ago.
**Perk (Marcin Stożek) | Elastic Ingest** 22:42 Oh, I see.
**Johanna Öjeling** 22:42 Hmm.
Oh, it's…
**Juliano Costa | Datadog** 22:44 called Dynamic Declarative Configuration Spec Types page.
**Johanna Öjeling** 22:48 And…
**Juliano Costa | Datadog** 22:50 It was… No, yeah, no, it's, I think Jay DeLuca… We have a PR.
One sec, let me know, sure.
Cool. I'll add to the docs… But then now on the mini notes.
**Johanna Öjeling** 23:19 Oops.
**Juliano Costa | Datadog** 23:40 Cool.
Cool, cool, cool.
Maybe… Johanna, I don't know, are you still… so this… is this your last week?
**Johanna Öjeling** 23:53 Ericia.
**Juliano Costa | Datadog** 23:53 Yeah, okay. I don't know if Jay is, on this time… time frame. Maybe we could ping him and… Asked if he could join one day, on our…
**Johanna Öjeling** 24:06 Yeah.
**Juliano Costa | Datadog** 24:06 on our call to at least discuss a bit, because I think that that idea goes Directly to… it is directly connected to what we are discussing here.
**Johanna Öjeling** 24:16 Yeah, and I think that that PR is a great reference to… To… yeah, For what we're trying to achieve.
**Juliano Costa | Datadog** 24:30 Cool.
**Johanna Öjeling** 24:31 How did you, find.
**Juliano Costa | Datadog** 24:35 So, that, that, that was the…
**Johanna Öjeling** 24:37 page.
**Juliano Costa | Datadog** 24:38 That was the fun part. So I was working on the telemetry level thing, and I wanted to get some reference on the configuration, on the declarative configuration file.
And I was navigating the page, and then I came across this page, and I was like, oh, this is cool. And I clicked through and everything, but then, yeah, I forgot to save the link, of course. But thankfully, the history of browser said…
**Johanna Öjeling** 25:06 - Yeah.
Yeah, that's really cool.
**Juliano Costa | Datadog** 25:15 Okay.
**Johanna Öjeling** 25:16 is also in Europe.
**Juliano Costa | Datadog** 25:20 Okay.
**Johanna Öjeling** 25:21 So, yeah. Yeah, so probably, yeah, I can check. Probably.
We can't join, this might take some time.
**Juliano Costa | Datadog** 25:32 Cool.
I want to also add… I saw… Was it you, Park, adding the events?
**Perk (Marcin Stożek) | Elastic Ingest** 25:46 Yes, everything.
**Juliano Costa | Datadog** 25:48 Okay.
**Perk (Marcin Stożek) | Elastic Ingest** 25:48 Yeah, unfortunately, unfortunately, the… I think the… cloud-native days, Denmark, and Poland are at the same time.
**Juliano Costa | Datadog** 26:01 And what?
**Perk (Marcin Stożek) | Elastic Ingest** 26:02 I think they're at the same… at the same time.
No, this is October. Oh, okay, so I made a mistake. One is October, Polish is October, Denmark is November.
A week after Click on.
**Juliano Costa | Datadog** 26:14 Who might be here also the… PCD portal.
I was there.
here.
**Perk (Marcin Stożek) | Elastic Ingest** 26:19 Oh, nice.
**Juliano Costa | Datadog** 26:20 Also, good event.
So… So yeah, it would be nice to share some… some of the things we are doing here. I mean.
like, some… maybe some highlights of, the stories that we… we heard, like the Skyscunner, Adobe, like.
And even, like, the three ones that we already published, that we can talk publicly, we could come up with, I don't know, something to also raise awareness of our work.
Yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 27:06 Hmm, that's actually an interesting idea.
Well, definitely.
**Johanna Öjeling** 27:09 point.
**Juliano Costa | Datadog** 27:10 Yes.
**Perk (Marcin Stożek) | Elastic Ingest** 27:12 Maybe we can do a joint session next KubeCon in Europe.
**Juliano Costa | Datadog** 27:17 Then, yeah, that will be cool.
Okay.
**So… Perk (Marcin Stożek) | Elastic Ingest** 27:24 Hi.
**Juliano Costa | Datadog** 27:25 to be the… Perk (Marcin Stożek) | Elastic Ingest 27:26 TBD, exactly, yeah, yeah.
**Johanna Öjeling** 27:28 I like that idea.
**Juliano Costa | Datadog** 27:30 And it will be Barcelona, so yeah, I'm not going just for QCon.
Top of days extra, for sure.
**Okay, KCD Portal, the CFP is still open, so… If you… Perk (Marcin Stożek) | Elastic Ingest** 27:54 It's November 19th, I can see.
**Juliano Costa | Datadog** 27:58 Yeah, it's 2 days, 19 and 20.
**Perk (Marcin Stożek) | Elastic Ingest** 28:04 Okay… And CFP is open until… Where is it?
**Juliano Costa | Datadog** 28:12 Till… 15th of July.
**Perk (Marcin Stożek) | Elastic Ingest** 28:16 Okay.
**Juliano Costa | Datadog** 28:17 I'm adding the link here.
**Perk (Marcin Stożek) | Elastic Ingest** 28:25 Nice.
**Juliano Costa | Datadog** 28:32 Cuckoo.
Then… Yeah, I think that's, I don't have any… Anything other than the promise that I will work on the telemetry-level ideas?
Idea.
**Johanna Öjeling** 28:48 I don't have anything else.
**Perk (Marcin Stożek) | Elastic Ingest** 28:52 So I have only promise of my key clock, but not this week, and then not next one. By the way, next one I will not be able to join because of travel, company travel, so I'll see you in two weeks, then.
**Juliano Costa | Datadog** 29:02 Actually, I'll try to put the dock on and update you all, async.
But next week, in the following one, I won't also be able to… to join.
**Perk (Marcin Stożek) | Elastic Ingest** 29:15 I see, okay, so… summer.
**Juliano Costa | Datadog** 29:17 Doesn't it?
**Johanna Öjeling** 29:21 And yeah, I'm not sure during my PTO, I may be traveling also, so I'm not yet sure, like, which of the meetings I'll be able to… but yeah, possibly… possibly we'll cancel next week, if neither of you can make it, so… Perk (Marcin Stożek) | Elastic Ingest 29:36 Yeah, yeah, yeah, yeah.
Definitely, you know, do it, like, summertime, take some time off the computer, right? Yeah.
**Johanna Öjeling** 29:45 Yeah, spend time on the beach instead.
**Perk (Marcin Stożek) | Elastic Ingest** 29:50 Sure, we deserve that, don't we? Unless there's a.
**Johanna Öjeling** 29:56 the Kiklo.
**Perk (Marcin Stożek) | Elastic Ingest** 29:57 blog post at some point.
**Johanna Öjeling** 29:58 Oh, yeah, exactly.
**Perk (Marcin Stożek) | Elastic Ingest** 30:00 Okay.
It'll be time for me then.
**Juliano Costa | Datadog** 30:03 Awesome.
Well, then, have a great rest of the day. See you all in a couple of weeks.
**Perk (Marcin Stożek) | Elastic Ingest** 30:12 See you around 14.
**Johanna Öjeling** 30:13 Good to see you.
**Perk (Marcin Stożek) | Elastic Ingest** 30:13 Yeah.
Given that…
**Juliano Costa | Datadog** 30:14 Cheers. Bye.
