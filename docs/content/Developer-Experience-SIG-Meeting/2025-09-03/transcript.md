SIG: Developer Experience SIG Meeting
Date: 2025-09-03
Duration: 26 minutes
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 01:10 Hello, hello!
**Damien Mathieu** 01:14 Hey!
**Juliano Costa | Datadog** 01:18 Good morning.
**Tristan Sloughter** 01:20 Good morning.
Nice soundproof room, I like it.
**Damien Mathieu** 01:29 Yeah, my co-working space has those, like, small, phone.
**Tristan Sloughter** 01:33 good.
**Damien Mathieu** 01:34 rooms.
I'm not in a recording studio.
**Juliano Costa | Datadog** 01:40 But it's nice that you can screen inside.
**Tristan Sloughter** 01:43 Hmm.
**Juliano Costa | Datadog** 01:45 Fantastic.
**Tristan Sloughter** 01:46 I'd work in there all the time.
Oh, we have someone new?
**Juliano Costa | Datadog** 01:54 No, hello!
**Tristan Sloughter** 01:55 Hi.
**Bogdan Nicolae Stancu** 01:56 Hello. Hello.
**Damien Mathieu** 01:58 Hello. Can you hear me?
**Tristan Sloughter** 02:00 Yep.
**Bogdan Nicolae Stancu** 02:01 No, okay, good.
**Tristan Sloughter** 02:06 We can kick it off with, I guess… So, I'll do the… We'll do blog post updates, and then, We can see what other topics might be there.
I don't really have much of an update on… blog post, I was kind of waiting, is there anything new from setting up a meeting with Mastodon to do… Nope.
**Juliano Costa | Datadog** 02:35 So, I still need to ping them and see. Yeah, I was a bit busy this week, presenting at, Container Days next week, so…
**Tristan Sloughter** 02:45 Oh, okay.
**Juliano Costa | Datadog** 02:46 if they replied, hey, let's do something next week, and I wouldn't be able, and then it would be, like, two more weeks to get another answer, so I'm just waiting to…
**Tristan Sloughter** 02:57 Okay.
**Juliano Costa | Datadog** 02:58 the textbook.
**Tristan Sloughter** 03:01 Yep, I figured the plane still is to… try to roll them out each week, so we'd start with Mastodon, so… not really… Pushing myself to knock out… the Atlassian blog post, but maybe I should, just so we have a… Template-type thing that we can go off of and discuss, so… Maybe I'll just… Try to write that up.
Was there anybody else we were talking to? You were…
**Juliano Costa | Datadog** 03:33 Yeah, I have… I have with me, remember to… Where are my tickets?
We did an interview with… Jeez.
I'll just mine on my… But we had another one.
**Tristan Sloughter** 04:01 Do I, do you mean the Skyscanner one?
**Juliano Costa | Datadog** 04:03 Yes.
**Tristan Sloughter** 04:04 Is there another… Exactly, yeah, yeah. Okay.
**Juliano Costa | Datadog** 04:07 So, yeah, that's on me, so I'll sit and write that one.
**Tristan Sloughter** 04:14 Yeah, but yeah, no… big rush, because hopefully we can get Mastodon first.
Maybe I can… Work on, like, the… introductory paragraph to the Mastodon one, so we can go over that, too.
Yep.
I can work on that.
Oh, thank you, whoever filled out the attendees.
See.
**Juliano Costa | Datadog** 04:45 words…
**Tristan Sloughter** 04:46 What's it?
**Juliano Costa | Datadog** 04:47 No worries, I didn't. One, one thing that… okay, yeah, wrap up.
**Tristan Sloughter** 04:55 I was gonna say that for, for Bogdan, that… so we're working on a… Blog post to cover different production setups of collectors that, but… companies use In the real world, because that was something that we uncovered in the surveys we did, the developer experience surveys.
And so this is… we're doing interviews with different companies to cover, how they… How they set up and maintain the collector in their companies.
**Damien Mathieu** 05:27 I think I would actually go also the other way, so, hi, Bogdan. I don't know, what, kind of, what prompted you to join this meeting? And, yeah, If… if it's because you have questions, or you want to give help, and yeah.
**Tristan Sloughter** 05:49 Yeah, well, I… for our next topic, essentially.
What brings us to the.
**Bogdan Nicolae Stancu** 05:56 Just as a presentation, I'm a developer for Adobe in the observability team.
And yeah, we use a lot of OpenTelemetry, and I kind of started, like, a month, a month and a half ago, contributing, trying to fix stuff, and understanding the project, because we… we have a pretty big deployment, and I feel like we're not understanding it properly, like, what's behind it, so I wanted to be that person that actually understands what we're running. And I do that by Whoa.
Fixing stuff, contributing back.
And I got into the whole Potterimetri project, and I… well, this is me, kind of, trying to understand what's happening in this meeting. I didn't have any expectations.
Sounds like something that I would want to see, a developer experience.
I think I joined another one, but It wasn't for this time zone.
Which, oh, yeah. I just followed it, mostly.
**Tristan Sloughter** 07:02 Yeah, developer experience is… We're… trying to tackle… the thing that's commonly heard is OpenTelemetry is complicated and hard to use in all the aspects, from the collector, the API, the SDK, so I set out to… Try to work on some of those, and we started out with a developer survey to get feedback, and… From that, we started this collector initiative.
To help.
with the ease of running the collector, and we might tackle some other things around API SDK eventually.
There's just a few of us, so we're taking it slow. You're at Adobe, do you know Greg Mefford? Meff? Meford?
**Bogdan Nicolae Stancu** 07:47 No.
**Tristan Sloughter** 07:48 Oh.
**Bogdan Nicolae Stancu** 07:49 is big, and I am…
**Tristan Sloughter** 07:51 Yeah, exactly. You…
**Bogdan Nicolae Stancu** 07:53 Hello, everybody.
Hey, Bishop.
**Tristan Sloughter** 07:55 Yeah, he works in OpenTelemetry, so…
**Bogdan Nicolae Stancu** 07:57 Oh, okay.
**Tristan Sloughter** 07:58 Yeah, the… he's… Mainly focused on the Erlang and Elixir.
API SDK.
Because they used that at… so Frame.io was bought by Adobe.
And… they use Elixir, and so he mainly works in there, but yeah, he's part of the OpenTelemetry SIG for Arling and Elixir, and he's working on, like, profiling our implementation of that signal. Might be someone good to connect with if you're interested in OpenTelemetry at Adobe.
**Bogdan Nicolae Stancu** 08:32 Yeah.
**Tristan Sloughter** 08:34 Absolutely.
**Juliano Costa | Datadog** 08:34 Another thing that I want to say is that maybe Adobe's a good candidate to… to write about.
**Tristan Sloughter** 08:42 I think I asked… Greg about that, and they're huge, so they'd be another, like, Atlassian one. Do you know how many, like, collectors you're running, and how many different types of collectors?
**Bogdan Nicolae Stancu** 08:55 I'm the one, kind of, managing all that.
**Tristan Sloughter** 08:57 Oh, perfect.
**Bogdan Nicolae Stancu** 08:58 We are everywhere, essentially.
Like, as region-wise, we are everywhere, and we have… I'd say… close to… I actually have a number, but it's, like, 3,350… 3… 3,500 collectors.
In total, just… just my team. Well, we are the observability team for Adobe, which, like, everybody should use us.
But the… yeah, that's the scale.
**Tristan Sloughter** 09:31 Is that, like, a demon sets, then?
**Bogdan Nicolae Stancu** 09:35 No, just the… There's a whole pipeline.
Because we wanted to give the users Their own… we build a chart, and they have their own chart that they deploy in their namespace, which is kind of for them.
To manage and deploy, and then we have our own set of collectors, which week and week, I don't filter stuff if they send random blogs.
And then, from that namespace managed by us, stuff gets to the backend.
**Tristan Sloughter** 10:09 The chart method might be something interesting to cover. We haven't had another, user who's…
**Bogdan Nicolae Stancu** 10:18 Gone that route, where they provide teams a chart that they deploy.
**Juliano Costa | Datadog** 10:22 Yeah, this sounds like a platform engineering approach.
Where you provide stuff for the other teams that are using.
I like that as well.
**Tristan Sloughter** 10:34 Mmm.
That might be worth talking about. That could go, I can't remember what Skyscanner's scale was.
But they're probably… they're in that range. Not Atlassian range quite, but the… I think.
So that could be, yeah, would you be interested in discussing, at another time, the.
**Bogdan Nicolae Stancu** 10:56 different…
**Tristan Sloughter** 10:57 You know, we would… We have questions about, like, team structure… company structure, so how the teams interact with you, Oh, do you have the perfect…
**Juliano Costa | Datadog** 11:08 Yeah, yeah, I sent out the… the SIG meetings.
Doc, but if you check on the document tabs on the left, there is the blog post outline.
And here is basically what we want to cover and discuss.
**Bogdan Nicolae Stancu** 11:24 Oh, okay.
Yeah, of course.
**Juliano Costa | Datadog** 11:29 I mean, mainly is what Tristan was saying, like, how you are using the collector, how you are deploying collectors, different types of collectors, the deployment.
That you are choosing, tips that you would give to users, because I think that was what Tristan was saying in the beginning. This was one of the pain points that we Got the most out of the research.
What happened was… people's… People said that it's easy to kind of get started, but… to actually have it in production, there are no best practices or recommendations or nothing online, so it would be great to have some kind of architecture reference or something, and this is the fort that we are trying to… to put here. The thing is that we want to kind of have different company sizes, so we could kind of say, hey, if you're a small company, maybe this setup would work best for you. If you're a medium-sized company, this other one. And if you're a big company, this is another reference. But, we want to start with the small one, and As they are small, it's hard to get them to kind of enjoy a call with us, so yeah, it's just.
**Bogdan Nicolae Stancu** 12:59 Makes sense.
**Juliano Costa | Datadog** 13:00 But yeah, this is the idea.
And of course, we are more than welcome to receive any other feedback that you may have, about pain points on using, OpenTelemry, because this is… I think our main goal as a sink.
Kind of to ease the onboarding and the developer experience to everyone that is actually using OpenTelemetry.
**Tristan Sloughter** 13:37 Yeah, do you get feedback? Oh, sorry.
Were you gonna say?
**Bogdan Nicolae Stancu** 13:40 I was gonna say that it was fine. The only problems that we have is because we have this chain collector set up from the user namespace to our managed namespace, and then the backend.
Any errors that the backend is giving are not, anywhere in the user namespace, because that transaction is already done. Like, if, we have rate limiting for metrics, and the backend is saying, no, you're sending too much. Our namespace sees the logs.
But the usernamespace doesn't, and we wrote something.
Internally to check this, like, before the user sends, it checks.
Limit range it, it is in, and it's just showing some logs, because you… Even though it's not… okay to do this, people still debug using logs a lot. Like, we provide the metrics, they can look at them, but they don't.
they just open the logs for the collector, they see that everything is fine, because that's the collector, that's what the collector is saying. Like, yeah, I sent it, it's fine, because it reached our namespace, the middle one.
And then they come to us, like, hey, what's happening? It's… everything is good, but I don't see my metrics. Where are them? And yeah. I mean, this limits one, it's just one. We also had an authentication problem, because we have an author proxy before the the backend, and that, again, is the same problem.
So yeah, I mean, I don't think it… Should be fixed. It's just something that… People should be aware of.
**Tristan Sloughter** 15:18 If you want to use this kind of setup.
Do you mean you're providing them with metrics about, like, dropped… their draft metrics, so they can see it? Yeah. Okay.
**Bogdan Nicolae Stancu** 15:27 Yeah.
**Tristan Sloughter** 15:28 Well, yeah, that's also an interesting story to tell about how you provide, developers with observability of… the observability pipeline, so they can, Even if they're not currently, we get to still talk about, what you've.
**Bogdan Nicolae Stancu** 15:46 We don't have, we don't have metrics for the dropped, well, they do have in their… if they want to set up a Prometheus and want to order them collector, they can do that. But we… the metrics that we provide are the ones that the backend dropped because of rate limiting. So they… I mean, they can see that.
**Tristan Sloughter** 16:06 They can see that.
**Bogdan Nicolae Stancu** 16:07 They can. They can see it in the metrics, they can look at the fact that they have dropped metrics because of unauthentication or rate limiting, but they… most of them, let's say, don't do that.
**Tristan Sloughter** 16:19 Yep.
**Bogdan Nicolae Stancu** 16:20 It's hard to move from logs to metrics.
**Tristan Sloughter** 16:24 Still a nice thing to, you know, like, point out to… for other teams that might not have thought about that, who can… who can do the same thing, and hopefully their users too, like… Do you have teams, coming to you, I don't know.
what you're… what you all cover, but do they come to you with questions about how to use OpenTelemetry in, like, the API SDK level?
**Bogdan Nicolae Stancu** 16:48 No. Electric? No. Okay.
Now, we… other teams do other things, we just give them a chart, they fill two things up, and it's fine. It's a pretty minimal setup for.
Most of the users.
**Tristan Sloughter** 17:03 Nice.
**Bogdan Nicolae Stancu** 17:05 We do have the operator deployed everywhere, so they can randomly set up collectors if they want, but then it's on them. We don't have support for that.
**Tristan Sloughter** 17:13 Right.
Do you do any, auto instrumentation through those home charts? No. Oh, okay. Nice.
**Bogdan Nicolae Stancu** 17:23 Yeah, it's that chart that we give them.
Auto Instruments their app, deploys an agent inside the pod with the app, and then another collector Which… Like, it's not, like, the St. Paul.
**Tristan Sloughter** 17:37 Or is it?
**Bogdan Nicolae Stancu** 17:38 It's a… it's a different collector.
**Tristan Sloughter** 17:40 Yep. Which…
**Bogdan Nicolae Stancu** 17:42 The agent sends to that one, and then that one sends to our namespace, where we process it.
**Tristan Sloughter** 17:49 Yes.
Okay, yeah, this would be good to… Let's go over, I can… We could set up a time, or we… hmm… Should we maybe just use this time next week, if we don't think there's gonna be anything to discuss?
Aside from this, since…
**Bogdan Nicolae Stancu** 18:10 I'm fine with a different meeting.
Not just to hug this one.
**Tristan Sloughter** 18:16 Boop.
**Juliano Costa | Datadog** 18:17 I won't be here next week, but it's fine for me, because this meeting is automatically recorded, so I can So I can watch the recording afterwards.
**Tristan Sloughter** 18:29 Okay.
Well, maybe we should just… I mean, do you… plan to be able to make it next week? I mean, I know that's a week off, but…
**Bogdan Nicolae Stancu** 18:37 Yep.
**Tristan Sloughter** 18:38 Sure, maybe we should just… Yeah, we don't… we tend to just, right now, be discussing the blog post, because we… we're not… Branching out into many other things at the moment, because it's just us three, so… We're just working on that. So, yeah, we can just discuss.
**Bogdan Nicolae Stancu** 18:53 I could help.
I'm interested in helping everyone I can. If you want another person to do Whatever.
Just tell me.
**Tristan Sloughter** 19:01 Awesome, alright. Yeah, we can do… we can, discuss your setup and discuss, yeah, more how you might be able to help.
Certainly with reviewing blog posts, that's gonna be a big one once we… Start putting them out. Good.
**Juliano Costa | Datadog** 19:21 So, just one thing that I may have lost, you said today, now, Tristan, or next week, the…
**Tristan Sloughter** 19:29 Oh, next…
**Juliano Costa | Datadog** 19:31 Oh, okay.
**Tristan Sloughter** 19:35 You know, sometimes it… yeah.
Refresh on anything you want to discuss.
**Juliano Costa | Datadog** 19:47 There is one thing that I would like to ask you, Tristan. Would it be possible to promote Damien and myself as maintainers on the repo? I know that we don't have many stuff on the repo going on, but we don't have any permissions on there.
**Tristan Sloughter** 20:04 Oh, I thought you did, okay.
Yes.
**Juliano Costa | Datadog** 20:07 I thought I would be promoted when we got the message from… A couple of months ago.
**Tristan Sloughter** 20:15 Really?
**Juliano Costa | Datadog** 20:16 And we discussed.
But… yeah.
Nope.
**Tristan Sloughter** 20:22 Was that the… Thought you were… or are you an approver or something?
**Juliano Costa | Datadog** 20:27 Nope, not even that.
**Tristan Sloughter** 20:29 Nope.
**Juliano Costa | Datadog** 20:30 when we got the message from Trask, right.
**Tristan Sloughter** 20:33 relative.
Let me look really quick, and… If I remember how to do… Okay.
Yeah, I will get that done, I'll look into that.
They do that with Terraform now, don't they?
**Juliano Costa | Datadog** 21:03 Good question.
**Tristan Sloughter** 21:05 Oh, maybe I'll… I might have to ping Trask about it, because…
**Damien Mathieu** 21:10 No, people's roles are not handled in Terraform, you have to.
**Tristan Sloughter** 21:14 No, it's not.
**Damien Mathieu** 21:15 It's groups, permissions and repositories permissions, but not people.
**Tristan Sloughter** 21:20 Oh, okay, so you have to manually go into GitHub?
**Damien Mathieu** 21:23 Yes, you… when you go into GitHub and add someone to a group.
**Tristan Sloughter** 21:27 Alright, so I have to ask someone to do it anyway, so… Because…
**Damien Mathieu** 21:30 If you are in the maintainer group, I think you should be a maintainer of that group, and then you can add folks.
**Juliano Costa | Datadog** 21:37 Yeah, for the demo, I added, two, one a maintainer and one approver.
**Damien Mathieu** 21:43 The idea, generally, is that maintainers are maintainers of the maintainer group, which gives them permission to add people to any subgroups.
**Tristan Sloughter** 21:59 Alright, one second.
I'm just gonna get that done right now, since, yeah, I can do it.
Lots of things to click.
And it is… Done. Cool.
You should get invites.
**Juliano Costa | Datadog** 22:27 Yay, thank you.
**Tristan Sloughter** 22:29 I'll clean up… And eventually, other people in there, unless they decide to come back.
Hmm.
Is… is there anything else we should discuss today? I did talk to… person in the Ruby SIG, they didn't have much more information yet about metrics.
API SDK questions, so… Don't have… how much feedback on that yet? They're gonna circle back with, like.
they didn't have the use case on hand for deletion of instruments, and that's the big one where I… I don't know if that would ever get in, unless it has a really good… use case.
So, yeah, they're gonna come back with that, hopefully, if they… if there is one.
Anything else to discuss today?
Oop.
**Bogdan Nicolae Stancu** 23:37 Should I prepare something for next week? I don't know, have a list of stuff?
I don't know.
**Tristan Sloughter** 23:44 That you want to discuss and develop?
**Bogdan Nicolae Stancu** 23:46 No, no, you wanted to ask me stuff about our setup. Should I use something?
**Tristan Sloughter** 23:53 So yeah, if you look at the… the outline in the tab, in that doc, the… anything that… So there's, like, an ask of, Hotel bin.
for the collector, things like that. Like, I know, like, I know Atlassian wouldn't give us much of anything on what their collector actually looks like, but as much detail as you're allowed to give.
**Bogdan Nicolae Stancu** 24:19 Yeah, I'll have to figure that out. I have no idea, to be honest. I don't even know if I shared too much in this meeting. I don't know.
**Tristan Sloughter** 24:27 The… and then the… think about the things of, like, That you'd like to see? Things that are missing from the club?
**Bogdan Nicolae Stancu** 24:37 Come on.
**Tristan Sloughter** 24:37 Any tips where you're like, oh, this was something we ran into and we fixed already, so it's not a problem, but other people might run into? So just thinking about those kind of things.
And figuring out how much detail you can give us, and then actually having that ready, so you can give it to us if you're allowed to…
**Bogdan Nicolae Stancu** 24:59 Yeah, yeah. That'd be great.
**Tristan Sloughter** 25:01 Alright.
**Juliano Costa | Datadog** 25:01 Don't worry about the diagram. This is something that we're gonna do just for the blog post, the final one.
But, if you can… for instance, provide us, I don't know, some sample configurations, some hotel collector configurations that you use.
Of course, removing the private stuff and, like.
**Tristan Sloughter** 25:24 Things that are…
**Juliano Costa | Datadog** 25:25 specific to… to Adobe, but, like, the generic stuff that you use, that would be great.
**Bogdan Nicolae Stancu** 25:32 Yeah. Okay.
**Tristan Sloughter** 25:33 Yeah, like, snippets and stuff, if you have it. Yeah, it was… Skyscanner had an OTEL bin already, like a diagram of their collector, so they could share that. But yeah, if you don't have something like that already, you don't build it. But Yeah, so, yep.
**Bogdan Nicolae Stancu** 25:50 Alright.
Makes sense.
**Tristan Sloughter** 25:53 Oof. Alright.
**Juliano Costa | Datadog** 25:55 Thanks, everyone!
**Tristan Sloughter** 25:56 Yep, thanks.
**Bogdan Nicolae Stancu** 25:57 Thank you.
**Juliano Costa | Datadog** 25:59 Bye.
