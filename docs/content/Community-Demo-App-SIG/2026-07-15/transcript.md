SIG: Community Demo App SIG
Date: 2026-07-15
Duration: 31 minutes
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 00:36 Hello?
**Matt Wimpelberg** 00:38 You already know.
I am. I have a team meeting that I might have to jump to, but I figure I'll try to… Hop in, see if we can get this load generator over the line.
**Juliano Costa | Datadog** 00:52 Yeah, let's… Let's see who actually joins.
Yeah, I would love to have another approval other than myself, because I think now I'm already too biased to…
**Matt Wimpelberg** 01:09 Yeah.
So, who else can approve? I haven't looked at the… Hello.
**Juliano Costa | Datadog** 01:16 So we have — let me — let me — All, all names.
So Cyril is a maintainer, Pierre, maintainer, and Roger from Elastic, maintainer.
They can approve.
But also, Donald, peter, but he's on holidays, and Shanoi.
that usually join join the meetings is Donal and Shanoi.
Oh, well…
**Matt Wimpelberg** 01:50 I…
**Juliano Costa | Datadog** 01:51 Pierre as well. So let's see.
**Matt Wimpelberg** 01:53 I worked with Surreal at Grafana.
**Juliano Costa | Datadog** 01:56 He actually left Grafana, he's with me.
Oh, you were…
**Matt Wimpelberg** 02:02 I hate a dog.
**Juliano Costa | Datadog** 02:02 Yeah, yeah, yeah, you.
**Matt Wimpelberg** 02:04 Right.
**Juliano Costa | Datadog** 02:04 Okay, okay.
No.
**Matt Wimpelberg** 02:06 Oh.
**Juliano Costa | Datadog** 02:08 Great addition, actually. Of course.
**Matt Wimpelberg** 02:11 Of course.
**Juliano Costa | Datadog** 02:12 Yeah, he was great.
**Matt Wimpelberg** 02:16 It's funny being on opposite sides of the vendor ecosystem.
**Juliano Costa | Datadog** 02:21 I have colleagues that say that you change companies, but you continue with the same colleagues.
**Matt Wimpelberg** 02:30 Yeah, especially with this.
Yeah, so appreciate all the work, by the way, on this PR. I don't think you're kind of… stepping on my toes at all, because you mentioned that, but I appreciate the help, I'm learning a lot.
**Juliano Costa | Datadog** 02:45 Yeah. Thank you. Actually, yeah, I I felt that I I was.
Too much, sorry.
**Matt Wimpelberg** 02:54 No.
**Juliano Costa | Datadog** 02:55 I was fixing something, and then by the time I was about to push, I saw that you actually fixed the thing, and I said.
**Matt Wimpelberg** 03:04 Oh, I think the same happened with me, yeah.
**Juliano Costa | Datadog** 03:06 And then the same happened later and I was like, oh yeah, maybe I should.
Step away and and just let it.
Hey, Felix.
**FELIX GEORGE** 03:20 Hi. Hi, everyone.
**Juliano Costa | Datadog** 03:24 Felix is also waiting for the K6 PR to land, Matt, because he wants to add some load to the agent, to the Agentic workflow.
**Matt Wimpelberg** 03:35 Cool.
**Juliano Costa | Datadog** 03:36 But it would… it would be, useless work.
Putting on the current low cost.
I wonder, can we actually control which scenarios we… trigger based on… Hello. I think so, right? We can have a… feature flag, or environment variable that says, hey, we are running Agentic, or we are running Profiling, or we are running… Yes.
**Matt Wimpelberg** 04:11 So, since… since last week, we… we added… I added, like, the entry point, so the process will restart when you change the feature flags. So we… we could theoretically put breaks in the code to say, do this, don't do that.
**Juliano Costa | Datadog** 04:25 Mmhm.
**Matt Wimpelberg** 04:26 But is that something you'd want to do before we land this PR or after?
**Juliano Costa | Datadog** 04:32 I think I'm good with… merging this PR, releasing 3.0, and then working on, Working on the load to the Agentic.
workflow.
Any objections, Felix.
**FELIX GEORGE** 04:52 I I agree. I'm I'm okay with it.
**Juliano Costa | Datadog** 04:57 Yeah, because I think we are way over time to actually get the 3.0 released.
**Matt Wimpelberg** 05:06 You have a job.
**Juliano Costa | Datadog** 05:08 Yeah.
Donald, actually, I want to sync with you.
as you're here.
Did you have the chance to take a look again at the K6?
**Donal O'Sullivan** 05:24 No, no, not yet. It's, it's on my plate.
hoping to get to it ASAP, but I… yeah, I think all the feedback's been addressed that I had anyway, so…
**Juliano Costa | Datadog** 05:36 Yeah, there was just one that I didn't know, but Matt actually, Documented well.
On the increase on the collector.
**Matt Wimpelberg** 05:50 Yeah, that was an existing issue. I think it just got caught in the… in Claude as I was going through everything, so…
**Donal O'Sullivan** 06:01 Yeah, I haven't got a chance to take a look.
Just off the top of my head. So, the collector wasn't getting out of memory killed, though, right?
Interestingly enough.
**Matt Wimpelberg** 06:12 No.
**Juliano Costa | Datadog** 06:13 Thank you.
**Matt Wimpelberg** 06:14 I think it was just dropping traces, like, almost silently.
**Donal O'Sullivan** 06:17 Oh, right.
**Juliano Costa | Datadog** 06:18 Yeah, we have a memory… we have a memory… memory limiter, processor.
**Donal O'Sullivan** 06:22 Yeah, yeah.
**Juliano Costa | Datadog** 06:23 So it just drops data.
**Donal O'Sullivan** 06:26 Yep.
Yeah, that might… that makes sense, actually.
Because we were seeing issues downstream, with the product catalog not being instrumented.
I wonder, is that being… maybe that's not… maybe it's not similar, but yeah, yeah. No, makes sense. I'll… I'll read about it in the PR, I guess.
**Juliano Costa | Datadog** 06:48 Yeah, that was the only… thread that I didn't resolve.
So all all the others we actually result. And regarding the Ui.
We do not have a UI anymore, but we do have feature flags.
So you can turn on, off, we can increase browser traffic, and you can increase, What is it called? Met? It's like normal.
Traffic, what, what is, like…
**Matt Wimpelberg** 07:23 Which one?
**Juliano Costa | Datadog** 07:24 The… the normal one?
**Matt Wimpelberg** 07:26 Oh, flooding?
**Juliano Costa | Datadog** 07:28 No, no, no.
**Matt Wimpelberg** 07:30 browser.
**Juliano Costa | Datadog** 07:30 Oh.
**Matt Wimpelberg** 07:30 browser or.
**Juliano Costa | Datadog** 07:31 Yeah, it's under Yeah, there is the browser and the other. The other one is just load.
**Matt Wimpelberg** 07:36 Yes.
**Juliano Costa | Datadog** 07:37 Okay, yeah.
So yeah, we just see a spike on memory consumption when we increase browser views for toy users.
But still, when we go to, let's say, 8, which is the max that we set now.
It is still not, not even close to what we had with Locust.
Cool.
I would say.
**Matt Wimpelberg** 08:09 I think it's just Go versus Python, to be honest, giving us the biggest gains here.
**Donal O'Sullivan** 08:14 Yeah, Python's pretty bad.
For that,
**Matt Wimpelberg** 08:18 Apologies, I do have to drop for another meeting, but if you guys have any questions, I'll be in Slack. I think, Juliana, you can answer any questions as well, you've been reading the code enough.
**Juliano Costa | Datadog** 08:29 Yep.
**Matt Wimpelberg** 08:30 Every other week I'll be able to stay on for the whole Cool.
**Donal O'Sullivan** 08:34 I'll make this a priority to review. It's like the big thing for me was just like the lower memory CPU consumption. So yeah, really liking that. So yeah, thanks, Matt.
**Matt Wimpelberg** 08:47 Yeah, absolutely. Talk soon.
**Juliano Costa | Datadog** 08:50 Chase.
Let me open the Cmt. Notes here.
**Donal O'Sullivan** 09:09 Apologies, guys, I've been on PTO the last few weeks, so I'm kinda… I'm a bit out of.
**Juliano Costa | Datadog** 09:17 All good, all good.
Matthew Chennai.
myself.
and Phoenix.
and don't know. Where are you?
Yep.
I I think the So.
Two things that I… that I think is missing from for for the release. One is the K. 6 Pr. To be merged.
that's That's… I think it's in a good state.
But… As I already touched the PR as well, I don't want to approve my own work and merge it, so it would be nice to have someone else, taking a look.
And besides that.
I… one thing that I want to ask for you all is… regarding Jesus Christ. Where is my English?
Regarding, make… start some. I have.
Have a mate command to start everything.
like, as of today, we have the MakeStart that starts the full demo.
But the full demo is not the full demo anymore, because we have the Agentic mode.
We have the profiling mode.
And we have the full mode. So Agentic and Profiling starts the full mode as well, but there is no… Full, full with Agentic, Profiling, and Kafka and everything.
So… I think if people really have the the a powerful machine they can run like, I mean, I can run on my company laptop.
But I think it would be nice to have a command to run everything.
Okay.
**Shenoy Pratik Gurudatt** 11:29 We should do better in naming them.
Something like iPhone models, S, Ultra, Pro, Max, whatever.
**Juliano Costa | Datadog** 11:37 Yeah, exactly, yeah, yeah.
**Donal O'Sullivan** 11:39 Okay.
**Juliano Costa | Datadog** 11:40 Let's call it Full Ultra.
**Donal O'Sullivan** 11:44 Good, I understand.
**Shenoy Pratik Gurudatt** 11:45 Okay.
**Juliano Costa | Datadog** 11:46 Cool, ultra pro.
Okay.
**Donal O'Sullivan** 11:48 Max, Max Silicon needed to run this.
**Juliano Costa | Datadog** 11:51 Okay.
**Shenoy Pratik Gurudatt** 11:53 Yes.
**Juliano Costa | Datadog** 11:53 Okay, so I will end here.
**Shenoy Pratik Gurudatt** 12:17 I'm just thinking, should we rename… Full to something like base, or… Oh.
Something else, and then keep a new full, which is actually full.
That compasses everything.
**FELIX GEORGE** 12:31 Earlier, it was minimal, right? Start. There was a minimal option.
**Shenoy Pratik Gurudatt** 12:35 Yeah, there is already a minimal today as well. There's, like, very less, even Kafka has stepped out of it.
I'm just thinking, because the naming full being in between everything.
Might be a misnomer there.
**Juliano Costa | Datadog** 12:55 Yeah, no, I don't know.
Because that's gonna be a big change. Like, a muscle memory of MakeStart will… Yeah, my… yeah, I don't… I don'.
**Donal O'Sullivan** 13:15 Maybe we need, like, a GitHub issue to, like, have a discussion on it or something. I know we can do it here.
Like, for me, What?
Like, what do you normally run? Do you want to just run everything and have, like, the Agentic Shop?
and also have profiling running, you know, or do you normally have, like, just, like, the full… or the minimal ver… like, what we… What's the average workflow under? Can we kind of go from there?
**Juliano Costa | Datadog** 13:46 I usually run the full demo, but I don't know about other users. I mean, the full, not full anymore, because, yeah.
**Donal O'Sullivan** 13:55 That's what I mean, though, like, are you running… are you running profiling now all the time? Are you running the Agentic Shop all the… you know, which I suppose that.
**Juliano Costa | Datadog** 14:03 Yeah, and.
**Donal O'Sullivan** 14:03 That would, like, inform… Like, do we want to have them… for me, I like them separate, because I don't want, like… I don't want my… I have a… I don't have a Mac, I run Linux, so I don't want my laptop to take off.
Sort of hovering around the room, but Yeah, like, I don't mind if we just move it all to full, so whatever you guys think, but it's just my two cents, like, what…
**Shenoy Pratik Gurudatt** 14:30 Even I run the current.
Full that is there, without age intake and profile. Only when we are… Actually looking into something on profiles or agents, only… it's only then when I start using those.
But doesn't hurt to have a full full as well.
If people were trying it out for the first time and have the capacity on their laptop, we just want to go all in and see every feature that we have added.
Yeah, the naming is something that we can discuss, but yeah, I would…
**FELIX GEORGE** 15:03 But wouldn't it be the other way around? For the people who are trying it out for the first time, they will start with a base. If they want to add more, they will keep on, you know, they will check the makefile and add more stuff.
**Donal O'Sullivan** 15:17 Yeah, but like the base has no observability or anything. So like it kind of defeats the purpose in a way.
**Juliano Costa | Datadog** 15:26 But, I… I think the current MakeStart is actually good. It shows how the service is running. It has Kafka. If someone has limitations, they can start with the MakeStart minimal.
And if they want to see the extra stuff, they can start agenting and start providing. The main point here is that currently we have a compose.full.
**Donal O'Sullivan** 15:58 Mmm.
**Juliano Costa | Datadog** 15:58 That is not full.
And if we create a comment, like, make start full.
It will just call the other, like, the Agentic and the profiling mode, which is perfect from the Make perspective, but from the Compose files perspective, we have a misalignment on naming, so maybe we need to rename the Compose files to align with that. But I think I think this is like a minor thing like we can.
we can… I'll work on that.
I have one… well, actually, two requests, two asks, let's say. Let's put it that way.
**FELIX GEORGE** 16:51 I have a request on… I have added the documentation for OpenTelemetry.io.
But I didn't get, you know, I have addressed all the requests that was… that was raised.
But it's still stuck there. Like, do I have to do anything about it?
**Juliano Costa | Datadog** 17:11 Do you have the link? I can. I can go and approve right away. Sorry.
Yeah, I'm not…
**FELIX GEORGE** 17:19 I.
The tests are also stuck, so I don't know if it is in the correct shape.
I hope you.
that.
**Juliano Costa | Datadog** 17:29 Thank you.
**Donal O'Sullivan** 17:30 This is… Open source, it can… sometimes things can take a while.
**FELIX GEORGE** 17:36 Yeah, I'm fine with it.
**Juliano Costa | Datadog** 17:39 Mmhm.
I mean, I knew that the… I had to go back to your PR after you fixed this stuff. I… and… and I remember the 3.14… Python thing that I commented. So I had on my head that I had to go back and apply. But yeah.
Sorry.
**Donal O'Sullivan** 18:02 It looks like there's… there's a Chalin… Patrice Chalin? He's requested changes, so it's probably… It's blocked by him, I guess. You should be able to reach out to him in CNCF Sl.
**FELIX GEORGE** 18:15 Okay.
**Shenoy Pratik Gurudatt** 18:16 Yep.
**Juliano Costa | Datadog** 18:29 Okay.
I want… So I added 2 2 issues to the dock.
and I'll also add This one here. That's what we can review.
Sorry.
So I want. I I need input from from you all on 2 issues that see Joe Thomas raised.
One, I'm 100% against, but I'm happy to… Happy to, not, Happy to discuss and accept the majority of votes, like we do in democracy.
So the thing is, he's, he raised… I think he's the first one. He raised a PR to… Connect these pens from… Check out… to accounting.
and checkout and accounting, they go through Kafka.
We have this service in to showcase spin links.
If we do parent-child, then the whole purpose of the service is gone. Like, we do not need that service. It's just another .NET or another… Java service, we can drop it.
**FELIX GEORGE** 20:25 Okay.
**Juliano Costa | Datadog** 20:26 He's saying that whenever the message is 1… to one, we should do parent-child.
And, the spec recommends… 1 to N, or N to N, to be span links.
So, I'd rather… not take this PR and then rework on a way that we process the… the payments in a batch. So we, let's say, every 10 orders, we do accounting and fraud detection.
Instead of having, one-to-one, as we have now.
rather than linking the the producer with the consumer rather than connecting as parent child, the producer and the consumer.
I said that on the issue.
So, but I I would love other folks to chime in and voice anything like their opinions, or whatever.
Oh.
So… I'll adhere as… Ask for help.
Yep.
Oh.
Mmhm.
And on the second one, the 3669, Caesar is up is adding a second collector.
To the demo, or if we run as a profiling mode, it will —.
**Shenoy Pratik Gurudatt** 22:12 Third one.
**Juliano Costa | Datadog** 22:13 3rd, correct? Yeah.
will be the third collector.
So this second collector would be the collector to receive the telemetry.
So today we we do a anti pattern of sending the collector metrics to to the collector itself, and then the the collector metrics go through the same pipeline and export it. This is not recommended, but we do it Oh.
intentionally here to avoid having an extra collector, and the proposal from CJOE is actually splitting into another collector. My concern here is just adding an extra maintenance burden, because then all the forks will have to document This second collector as well, and then we would need to configure this second collector as well to export the telemetry to somewhere.
So it's not just one… Config.extra file that we would need to modify.
Would be now to config that extra.
If you all follow me.
So… this is just like it's a demo. Yeah, we. I think we even say there that this is not recommended. If we don't, we can add.
Where is it?
**Shenoy Pratik Gurudatt** 23:48 I am… Fine to not add the PR, the collector one.
It's not too much, it's not adding much value.
**Juliano Costa | Datadog** 23:58 What, sorry, come again?
**Shenoy Pratik Gurudatt** 24:00 I'm fine to not add this PR, which adds the new collector for self-telemetry. Not adding much value, as in that we are not showcasing anything new to the users.
That's the first thing. The second part is, as you mentioned, the maintenance burden itself.
If there was something new in config, like what we do with profiles, and there are some special permissions needed, then it would have made sense.
Because profiling itself needs some kernel access at times, some bytecode access at times, so it needs some special privileges.
But, that has some… Value to the users, but here it's… It's difficult to understand, do we even provide any value to the users?
go there, Demo.
**Juliano Costa | Datadog** 24:53 Yep, I I agree.
But, yeah.
But I… but I… the thing is that I don't want to be a… I don't want to be an asshole and keep saying, like, hey, no, don't do this, like, yeah, don't, don't, don't touch my demo, like, it's not mine, so that's the thing. I would love to have,
**Shenoy Pratik Gurudatt** 25:15 Oh my god.
**Juliano Costa | Datadog** 25:16 involvement from from other folks as well on those discussions.
**Shenoy Pratik Gurudatt** 25:22 I think on that, the second one, the counting and Kafka one, I did post it, saying 1 is to… because we are doing it currently 1 is to 1, it should be fine, but the ideal way is to go the batches with… Like, we could not… Do something that no one does in production.
zero, nobody consumes one message from a service, sends to Kafka, and then consumes it on the other end. It always batches, that's the whole point of queuing with messaging services.
**Donal O'Sullivan** 25:52 Yep.
**Shenoy Pratik Gurudatt** 25:53 So, yeah, I'm also fine doing that.
like doing the right thing first, rather than putting something in and then fixing it later. Fixing in later might not happen soon. That's the thing. Yeah.
Oh.
**Juliano Costa | Datadog** 26:10 Yep.
**Shenoy Pratik Gurudatt** 26:11 Okay.
**Juliano Costa | Datadog** 26:12 Okay.
Okay, okay.
Cool.
Great.
**Shenoy Pratik Gurudatt** 26:19 I'll post both the comments.
On the thread. Let's see.
**Juliano Costa | Datadog** 26:24 Thank you.
And just to bring another thing that Felix shared with me on on slack Felix.
So, Felix has a draft for, a blog post about the Agentic being added, the Agentic workflow being added to the demo.
Felix, do… I think… raising that on the OpenTelemetry.io would be ideal, right? I think, gives the whole hotel community visibility.
The only thing would be, We have the draft for the… For the 3.0 blog.
and we could… Maybe have that after, if that's fine.
**FELIX GEORGE** 27:19 Yeah, yeah, I'm fine.
**Juliano Costa | Datadog** 27:21 Cool, okay.
and I don't know if you want to share the draft with us, and we review before, or you can open the Pr. And then we review in the Pr. That both approaches are fine.
**FELIX GEORGE** 27:36 So, right now, I made… because, I was also thinking about OpenTelemetry.io, so I wrote it in the MD file format. I can share the file in the Slack.
I'm.
**Juliano Costa | Datadog** 27:48 No, it's fine. Let's just wait, and you open the issue, because then we can. We can review in a in a proper way. Yeah.
I saw that Shenoy commented on the on the draft.
donald, if you could also take a look, if you open the… If you open the the tabs that we have on the.
On the SIGMETI notes, There is a second tab called draft blog post.
**Donal O'Sullivan** 28:21 Yep.
**Juliano Costa | Datadog** 28:22 And I have, and I have a draft there. It's missing 2 things. One is the Open server.
That was added. And another one is, I'm gonna call it, if you have any better ideas, let me know, but I'm gonna call it the invisible work.
Peter from Splunk, he put a lot of work on reducing the vulnerabilities that we had on the demo.
When he started working, we had about 300.
And we are down to 8 or 6.
So if we go to It's the demo itself.
Yeah, 7.
If we go to the tab on the OpenTelemetry demo security and quality.
We have 7 code scanning issues, but, like, yeah.
none that we can actually solve at the moment.
He… he helped a lot, so I want to… I want to add some acknowledgment there. That's the whole point of the 3.0 blog, thanking the contributors and every — I have sections where I highlight the work of each one of us.
Oh, okay.
You are there on the profiling part with Rorian.
**Donal O'Sullivan** 29:57 Yep.
**Juliano Costa | Datadog** 29:57 Chennai and Felix on the on the Agentic and then Chennai on the telemetry.
Telemetry tests. Oh, man, the telemetry tests are so useful. Holy shit. It runs.
It is green, I just merged, and I'm… yeah.
**Donal O'Sullivan** 30:16 Yolande.
**Shenoy Pratik Gurudatt** 30:19 Yep.
**Juliano Costa | Datadog** 30:20 Thank you.
So… Yeah, and this is… something that we can improve on the way that we are building the images and stuff, but I think that's, That's, something to… to work after the… After the 3.0.
Anything we should wait, for 3.0 or…
**Donal O'Sullivan** 30:57 No, I don't think.
**Shenoy Pratik Gurudatt** 31:00 Let's cut this one.
**Juliano Costa | Datadog** 31:02 Yeah, I like that.
**Shenoy Pratik Gurudatt** 31:03 Basic fun as much.
**Juliano Costa | Datadog** 31:05 Cool, okay. So I'll wait on reviews on the K6.
I think, whenever I have the… the green check, I'll hit merge.
**Donal O'Sullivan** 31:22 Thanks, O.
**Juliano Costa | Datadog** 31:23 Ron?
And… yeah.
**FELIX GEORGE** 31:26 Goodbye.
**Shenoy Pratik Gurudatt** 31:28 See you.
**Donal O'Sullivan** 31:29 See you guys.
