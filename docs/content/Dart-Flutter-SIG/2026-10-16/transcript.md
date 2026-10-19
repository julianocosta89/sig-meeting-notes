SIG: Dart & Flutter SIG
Date: 2026-10-16
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Robert Magnusson** 01:04 Hello.
How are you?
Oh, you're muted, Michael.
Unmuted. Or it's, it's, Red, your microphone.
Or maybe it's only me.
**Michael Bushe (Mindful Software, LLC)** 01:28 Good morning, good morning.
**Robert Magnusson** 01:29 Now it's coming up.
**Michael Bushe (Mindful Software, LLC)** 01:30 Hope you guys are doing well.
**Robert Magnusson** 01:34 Yeah, all good. Very stressful week.
**Michael Bushe (Mindful Software, LLC)** 01:37 I didn't.
**Robert Magnusson** 01:38 I did nothing of my normal work. I just did like demo environment, demo videos preparation.
And I thought I was done, and this morning, apparently, some stuff didn't work, so I have to do even more.
So I thought I didn't do any at all of the old tableau work this week. I, I, yeah.
**Michael Bushe (Mindful Software, LLC)** 01:55 Hello?
No worries, I mean, we put out a couple releases, so, you know, taking a breath is, is probably not a bad idea.
**Robert Magnusson** 02:05 How are you guys?
**Michael Bushe (Mindful Software, LLC)** 02:10 How about you, Harshit? How are you?
**Harshit Kushwaha (OpenTelemetry)** 02:13 More everything.
**Michael Bushe (Mindful Software, LLC)** 02:18 I had on the agenda today. I did again. Why don't you, Harshit, if you're willing, can you?
talk to us about the about the organization you're doing in in our slack. What's going on there? This is due to me. I don't know. Maybe it's things I should know about, but I don't.
**Harshit Kushwaha (OpenTelemetry)** 02:37 Like, the workflows and channel managing.
**Michael Bushe (Mindful Software, LLC)** 02:43 This is just standard for all the Slack, groups, and… I'm an admin now, does that mean I have responsibilities, or…
**Harshit Kushwaha (OpenTelemetry)** 02:53 No, there are no such responsibilities, like, we have to manage workflows that we need for ourselves, like a meeting reminder, and we can also connect a GitHub repository for incoming issues and PRs related.
**Michael Bushe (Mindful Software, LLC)** 03:07 Oh, that's great! Oh, okay, I tried to do that before, and I was blocked, I couldn't figure out why, so I'm glad you figured that out. That makes things a lot easier.
That's cool.
**Robert Magnusson** 03:19 How does that work? Like, we get a ping done in Slack in, like, our Dart channel whenever there's a…
**Harshit Kushwaha (OpenTelemetry)** 03:25 Yeah, we can set up a workflow, like, you can use a webhook to set up a workflow from the GitHub repository. And it will message on the channel, or you can do it on your personal DMs also, like, it will work.
Like, we are the channel manager, so we can add any workflow, but we have to create them from scratch, because there is no SH template and… Things in the Slack right now.
So, we have to create the workflows from scratch, and using webhooks, we can use a GitHub repository, like the OpenTelemetry Dart repository, and it will message us regarding the incoming issues or PR, or we can add a weekly summaries, like, this PR is ready to merge, and this needs a review.
These are the incoming issues and all.
**Robert Magnusson** 04:12 Okay, cool.
**Michael Bushe (Mindful Software, LLC)** 04:13 Yeah, I'd be really hopeful.
**Harshit Kushwaha (OpenTelemetry)** 04:15 We are doing this, like, in collectorship, we are doing this same thing.
**Michael Bushe (Mindful Software, LLC)** 04:22 Feel free to keep going and connect it like other groups do. I'm sure that they… if they have workflows that work for them, it'll probably work for us.
Eli Bay, how are you?
So we released, the API and the updated SDK. Those are… those are in PubDev now. That's… that's really good news. I did make the API announcement. I didn't make the SDK announcement yet. I'm gonna… I'll put that on LinkedIn and X, and I really have to go to Blue Sky and start, publishing there.
I'll try to make sure I have everyone's, everyone's, links correct. I have… and I don't really know how to organize… I think I've got… I've got everyone's GitHub, right?
And I've got X… I just have a private repo where I keep this stuff, because obviously we don't want to make it too public. On the other hand, it's public, I don't know what we want to do with it. I have LinkedIn for… everybody here, and then some, and I have X for… Right, you don't have an ex-account, Robert, and LaPay, I don't have your ex-account either. If you want to slack that to me, that'd be helpful. And if anyone has a blue sky, I think I only have, Kevin Moore's blue sky.
**La Pyae** 05:52 I don't…
**Robert Magnusson** 05:55 That's our goal.
Go ahead.
**La Pyae** 05:58 Right on.
I pointed to you at Ace.
Okay. Last week?
**Michael Bushe (Mindful Software, LLC)** 06:06 Oh, was that a DM in… was it in LinkedIn, a DM? Did you give it to me?
**La Pyae** 06:10 Yes.
**Michael Bushe (Mindful Software, LLC)** 06:11 Yeah.
**La Pyae** 06:11 Also, also an ace, yeah.
Basically.
**Michael Bushe (Mindful Software, LLC)** 06:15 Okay.
**La Pyae** 06:15 On that, yeah.
**Michael Bushe (Mindful Software, LLC)** 06:18 All right, I'll take a look at that.
**La Pyae** 06:21 important.
**Michael Bushe (Mindful Software, LLC)** 06:22 That's right, now I remember, sure.
And, what was I gonna say about? Does anyone know who I am? Paradox is.
He may.
**Robert Magnusson** 06:34 know.
**Michael Bushe (Mindful Software, LLC)** 06:34 He made a few contributions, right? All I can see is his GitHub. I have no way of contacting him, but okay, that's all right. He wants to be mysterious. I like it.
Okay.
**Robert Magnusson** 06:45 Maybe it's like a broken out AI agent from OpenAI.
**Michael Bushe (Mindful Software, LLC)** 06:50 I'm right. Is he really there? Right.
The other thing I want to, I want to mention is that, we had a PR in the OpenTelemetry Dart repo, for the package doc that almost all of us have reviewed. I've merged that PR.
And so that's a doc you can see, and I put the link to that doc. So that's our first file, right? Yeah, that's really good.
And what I'm hoping, I know Yusuf is also busy. We're all very busy. I'm not pushing anybody.
the directory structure is next. I asked him to make a PR. I thought he did it, but maybe I missed something, because I don't see it there now. So I think that'll be coming. Usually he works on the weekends, so maybe that'll come this weekend or so. And then we can review our directory structure.
**Robert Magnusson** 07:49 Cool.
Then I'll keep an eye out for that.
Can I ask, according to the previous thing, the… so the… the pub.dev, the OpenTelemetry, which used to be WorkShiva, that's now pointing to Dartastic.
**Michael Bushe (Mindful Software, LLC)** 08:06 Wow, you're really quick. How did you know that so quickly? I did that last night.
**Robert Magnusson** 08:11 Aha, okay. Then I dreamt it, maybe, because I had something vague in my head that you posted it somewhere, but maybe… It was,
**Michael Bushe (Mindful Software, LLC)** 08:20 Unless you're…
**Robert Magnusson** 08:21 something…
**Michael Bushe (Mindful Software, LLC)** 08:23 I did post it, but I didn't think anyone saw it, and I still have to kind of update that doc, but if you're following the Dart… I don't… I'm not sure if I can… how much I can talk about, you know, our commercial stuff here, but I posted it on Dartastic, and so he… and I… and… What I want to… what I'm… alright, well, I might as well go into this. So, I took that package doc.
And I took the plan that we have in Slack.
And, I still want to update this doc a little bit, so I haven't announced it yet, but if you go to Dartastic, you go to the blog, you go to the most recent entry, there's some language that I want to clean up a little bit. But the whole plan is there.
And I worked with, Rob Becker from Workiva.
And I worked with, with, Andres. I can't remember his last name. 2 last names. He has 3 names.
who has the open dash telemetry packages, and now those are all under Dartastic, so we're sitting in them, we have control of them. As we move things, yeah, right, that's really good. And I also worked out… part of the plan, you'll see it in there.
And I worked it out with Rob, too, is he's gonna… he's gonna do it for… so we're Kiva, we don't want to break any… the main thing is we're not gonna break anybody, right? And we gotta… we don't have to be too careful.
OpenTelemetry can do what it wants, and then the other packages, mainly Dartastic, will have to… will adjust along the way, and the plan is described. We don't want to break anybody. To not break Workiva, they are on 018.0, and.
**Robert Magnusson** 10:06 the.
**Michael Bushe (Mindful Software, LLC)** 10:06 We are going to, A.
Sorry Rob has a has used AI to make a migration guide.
Well, let me put it this way. I'm gonna take the Beta 17 release that we have. I'm gonna publish that, even though it's 1.1 on ours, because I made a mistake a long time ago. I'm gonna publish it as 1.0 Beta 17.
**Robert Magnusson** 10:33 some.
**Michael Bushe (Mindful Software, LLC)** 10:33 is using that now, it'll roll with our changes as we roll. And I'll keep… just like I kind of cross-post down in Dartastic, I will cross-post across in this way.
For the 018 people, they won't… they won't see that, they're not broken, but, they will… get a doc update that has a migration guide and we'll point them to the new one.
**Robert Magnusson** 11:01 Okay.
**Michael Bushe (Mindful Software, LLC)** 11:01 And any other users will be able to see that.
So, meanwhile, as we… the first part is… the first one is semantics, right? This will be, like, sort of the… this will grease the skins for everything. This will put in practice our release and update structure. But basically, we'll get semantics in there. I don't know when we want to do this. We might want to focus on the tracking bugs. It's up to you guys, whatever you guys want to work on.
But the, I'm a little more focused on the… people are using it, so I'm focused on the quality.
it was interesting that, probably because of AI, and the reason why I stepped in so quickly, too, was, I was gonna let it go, but at one point, people… the adoption rate for Dartastic… Workiva went down, and Dartastic went up. And then I think due to AI.
Where Kiva, about a month ago, they were neck and neck, 50-50.
And then in the next in the last month, Workiva grew three times as fast as Dartastic. So, you know, it just made sense for tens of thousands of new users to be using a you know a stable.
**Robert Magnusson** 12:11 maybe.
**Michael Bushe (Mindful Software, LLC)** 12:12 Yeah, and not stable, but near.
**Robert Magnusson** 12:14 Yeah.
**Michael Bushe (Mindful Software, LLC)** 12:14 compliant.
**Robert Magnusson** 12:17 And one that is maintained or it's moving forward.
**Michael Bushe (Mindful Software, LLC)** 12:20 Yeah, exactly, exactly. And they only had traces, which is not at all compliant, but it works. And alpha metrics and alpha logs. So, it's definitely good for the community to have all of that.
The what else was I gonna say about that?
Right, so because people are using it, I'm gonna be… whatever time I have going forward, I'm gonna be focusing on PRs for the STK. We'll be improving quality.
when we close that, the idea is that, and this is, this is on that doc… oh, so I have the po… I have the doc in Dartastic. What I promised Severin, was, I will then make another doc that is not It takes out some of the commercial stuff right? And I'll post that to the open telemetry blog saying, this is what our our project's goal goals are.
And Then Right? And where was I going with this? I had another thing I was going to say.
Right, and so that plan is basically… and I think we've talked about that before, but we might as well say it in the meeting, just to make sure everyone is on the same page, and hey, plans can be changed, too, if anyone has a good idea. But I think we close the tracker.
We run another set of AI updates. And as I mentioned, this will be smaller because we fixed so many bugs, but larger because the AI gets smarter.
**Robert Magnusson** 13:59 Yeah.
**Michael Bushe (Mindful Software, LLC)** 14:00 Right? So, we'll see what… we'll see how that shakes out. I suspect we're gonna have two more rounds of this.
AI, I'm sorry, API bugs to fix, SDK bugs to fix, and maybe another round. And then, like, okay, so if AI finds anything by then.
Well, you know.
**Robert Magnusson** 14:20 Yeah, I always find something, some edge case, edge case, edge case. That doesn't really happen.
**Michael Bushe (Mindful Software, LLC)** 14:26 Right, I've never seen a software without bugs. I think after that third round, we'll be better than all… and my goal, as I stated, is, and I hope the team accepts it, but at least it's my goal, is to be better than all the other SDKs. We don't have… we don't have weights, we don't have any debt, to pay, and we're using AI, so there's no reason why we shouldn't be just as good if not.
And the others.
**Robert Magnusson** 14:50 Yeah, and we have all the other ones as references also, which is also nice. You have something to compare against, like, quite stable Go or Java versions.
**Michael Bushe (Mindful Software, LLC)** 14:59 Right? Yeah, yeah, yeah, so we can cheat by looking, by looking.
And another thing, too, for people who want to contribute something that's open right now. Well, I guess this is probably for later on. But I want everyone to be aware that the open telemetry has a demo. It's an open telemetry demo. It does meteor. No, what is it?
Saddle, planets or something like that, astronomy or something like that, and every single piece of OpenTelemetry SDK for every language is included, and so we should have, we should… you know, someone… this would be fun, I think, if someone wants to take it on, that's a nice, nice thing, and maybe that should wait until…
**Robert Magnusson** 15:45 And that's not… that's hosted in some sort of OpenTelemetry examples repo. It's not in each language.
**Michael Bushe (Mindful Software, LLC)** 15:54 Correct. It's just one big one. Yep, and I think it's called open telemetry dash demo.
**Robert Magnusson** 16:00 Okay.
Yeah, that makes sense.
I mean, that's a fun part also, building apps.
**Michael Bushe (Mindful Software, LLC)** 16:08 Yeah, I think the demos are critical. In the Dartastic open source repo, I also have, and I'm going to keep there, a Dart OTEL reference demo.
And that is intended to not only just show that, hey, this works, but to show all the best practices and to show some Flutter best practices.
**Robert Magnusson** 16:34 Yeah, like a reference implementation.
**Michael Bushe (Mindful Software, LLC)** 16:38 Right.
**Robert Magnusson** 16:39 Probably also maybe have something like that in the OpenTelemetry Dart repo also, right?
Bundled with the code, like, directly there, an example, huh?
**Michael Bushe (Mindful Software, LLC)** 16:48 If someone…
**Robert Magnusson** 16:49 Yeah, like, one stop.
**Michael Bushe (Mindful Software, LLC)** 16:51 I've already done my demos, so if someone else wants.
**Robert Magnusson** 16:53 Yeah.
**Michael Bushe (Mindful Software, LLC)** 16:54 It was better to have two than just for me to just copy those over. And I'm going to maintain those separately. And I also add in things that probably wouldn't go into the OpenTelemetry one, like a server pod, which is commercial, server pod demo, Dart functions in GCP, which is commercial, so that wouldn't go in there, things like that.
**Robert Magnusson** 17:18 I could go in, I guess, some sort of lightweight Dart backend also to show, like, sort of both paths. Show, like, the Auto Dart server, the Auto Dart Flutter, plus also then spinning those up And having, like, the end-to-end traces also between them, so that you could…
**Michael Bushe (Mindful Software, LLC)** 17:32 else.
**Robert Magnusson** 17:32 Locally, and just,
**Michael Bushe (Mindful Software, LLC)** 17:34 Using Shelf, because that comes from the Flutter team, I assume it's some kind of MIT or Apache. We'd have to check with the license.
Or does it have to… I don't know, that's the work, right? Does it have to be purely open telemetry and, you know, we're coding network calls, and we're coding a router, you know?
I don't think so. I assume Michelle.
**Robert Magnusson** 18:00 Yeah.
**Michael Bushe (Mindful Software, LLC)** 18:00 shuffle.
**Robert Magnusson** 18:02 Cool, yeah, it's not urgent though, but I think makes sense to have some sort of example in there.
But you can… also for us, like, for anyone contributing, you can also directly then validate in the example app that it works in some sort of real application.
**Michael Bushe (Mindful Software, LLC)** 18:18 Great.
**Robert Magnusson** 18:20 Cool.
**Michael Bushe (Mindful Software, LLC)** 18:23 Anything else?
**Robert Magnusson** 18:27 Mmm… No, so next big steps, that's then, getting the directory structure in place.
**Michael Bushe (Mindful Software, LLC)** 18:37 Yeah.
**Robert Magnusson** 18:38 That's right. Yeah, sorry.
**Michael Bushe (Mindful Software, LLC)** 18:40 you want to lean on Yusuf? I know he's really busy during the week.
**Robert Magnusson** 18:46 good.
**Michael Bushe (Mindful Software, LLC)** 18:46 And he's told me he's, he's, doesn't have too much time, for, for it. I know he wants to do it. And he's done, he's done good work and he already had the plan. So I don't know, figure it out. Like if you, if, if he, you know, maybe give him, you know, a week or two, I don't know. And if not.
**Robert Magnusson** 19:04 Yeah, maybe that's nice. Not swoop in and just take it over and give him some time to catch his breath.
**Michael Bushe (Mindful Software, LLC)** 19:09 Right.
**Robert Magnusson** 19:09 And implement it, and then maybe in the next sync, if nothing happened, we can see if we should,
**Michael Bushe (Mindful Software, LLC)** 19:14 Yeah, there you go, there you go. I think he'll do it. He did say he would, so yeah, let's give him a chance.
**Robert Magnusson** 19:21 Cool.
Sounds good.
**Michael Bushe (Mindful Software, LLC)** 19:23 Anything about the open PRs? I haven't looked at anything in the… I know we have the AnyValue PR, which I want to look at again, in the API, but right now I'm focused more on the SDK. I haven't looked at the… what's out there? Anything interesting, or… Nothing controversial.
**La Pyae** 19:46 Nothing to talk, anything? Yes.
Of this week, and… I tested with… I tested with, Grandpa, Grandpa, that Hasid, Hasid told me, you, you can go to, like, I test in my application, but, for now, I, I didn't come any better, but… I'm trying to implement, and what's going on. Yes, I'm checking this.
That's an interesting part.
**Michael Bushe (Mindful Software, LLC)** 20:20 That's a good way to do it.
**Robert Magnusson** 20:26 Oh, yeah, so I didn't check anything last week. I will try to catch up. I think I'm… The weekend, I cannot work so much, but on Monday, I will catch up on on the current state of things. If you need something, then just ping me in Slack there, and I will look into it.
**Michael Bushe (Mindful Software, LLC)** 20:43 And I actually put a lot of work in this week, so I'll probably be doing less next week, so… So.
**Robert Magnusson** 20:51 Well deserved.
**Michael Bushe (Mindful Software, LLC)** 20:53 you Yeah, well, thank you all. I have to… you guys make me work so much because you're doing so much work, and I have to release it and document what we're doing. So it's good to see this forward progress and the community. The other thing, too, and one other thing I want to mention is community. We want to grow the developers that are working on this, we want to get more contributors, so… talk to your friends, talk to your folks in social media, and say, hey, we've got this interesting project going on, it's fun to work on, would you guys like to help out? We really… we have a tiny… compared to other Teams, we're tiny and we should be bigger and that will drive up community adoption. I've reached out to Google to see if they'd give us some Flutter expert time. I haven't seen that yet.
I reached out again, but I'll keep hinting about it. So I think… and the other part of… I think what will happen… so we just got to get mindshare around it, and so I will, and you guys please also.
I noticed that Harshit posts about OpenTelemetry a lot. make posts on all your social media, and say, hey, look, we got this going on, and what I'm going to do… my next… contributions. Just keep. I want to say something else that I've written too much code, and you know I don't write as much code anymore because everyone has to get the mindshare in the code, so I'm working on sort of the other parts, right? And the next part is, I'm going to take those demos that I have, and I'm just going to keep posting, oh, here's how basic distributed tracing works, isn't that cool? Oh, here's how you use AI in your local development with this tracing, right? And so I think as those things get spread around, and we start to gain mindshare, hopefully people will come onto the project. I try to mention the How people can join on everyone.
**Robert Magnusson** 23:02 Cool. Yes, I also, on that topic.
So, at Grafana, we're wrapping up, like, our first exploration on mobile observability this year.
And I plan to do some, like, meetups, Flutter meetups.
next year, spring. I know… I know Munich Flutter Meetup, which is quite big, and there's a lot of Flutter developers in Germany.
I hope also next year to go to the… there was just a FlutterCon in Berlin. I couldn't make it this year, but I hope to go next year.
So I will try, at least in German space, to get my foot in beginning next year into some meetups and start talking about OTEL, OTEL Dart and Flutter, and try to sort of get the attention there, because there are some big players, I think, in Germany.
using Flutter.
**Michael Bushe (Mindful Software, LLC)** 23:47 Yeah, Flutter's really big in Europe, for sure. Yep.
I had started to make a Florida Flutter meetup when I was in Florida, but I left before I really could get it going. But I'll also try to get to some of the… a lot of the… even though I'm in France, I can, I can do… a lot of these Flutter meetups are remote, so maybe I'll try to do that, too. Right, that's a really good way, because then you know you have a.
People who are there who want to learn.
what we have.
**Robert Magnusson** 24:19 Yeah, I think so, too.
Especially then, if we bump it, we need, like, Hide the complex.
Flutter terminology, attributes, exporter, pipeline, and just expose as lightweight as possible, digestible for people, like, a few lines set up, and then having that nice integration with my BigO router or something, that they auto-record your view navigation for you, and.
**Michael Bushe (Mindful Software, LLC)** 24:45 I think we're gonna get a lot of traction once we, once we go there, right? And there is, there is the, auto, sorry, GoRouter is there. It will auto-record. That would be a really good demo to have, if somebody wants to make one. Maybe that would be one for.
For, the open telemetry demo.
And then AutoRoute is another, but I… and I think the only demos that I have in Dartastic just simply use Navigator, which nobody uses, so that's it. But yeah, I think we really have to go kind of up from Dart into the Flutter land before we get too much… before we're gonna get…
**Robert Magnusson** 25:21 Yeah.
**Michael Bushe (Mindful Software, LLC)** 25:22 Many people jumping on.
Alright, cool, everybody. I'll give you back a few minutes. Good to see you guys this week.
**Robert Magnusson** 25:33 Have a nice weekend, then. Talk to you online. Feel free to ping me if there's anything, then I'll jump onto it.
Bye bye.
**La Pyae** 25:39 Okay.
**Michael Bushe (Mindful Software, LLC)** 25:41 Bye. Here.
