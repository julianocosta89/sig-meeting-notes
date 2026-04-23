SIG: Community Demo App SIG
Date: 2026-04-22
Duration: 30 minutes
Zoom Recording URL: https://zoom.us/rec/share/j7uG5QVHtiQoVQrqXfcW2K5zkXbJwvMk9gL_3BAamY2kVKgN6eEmj5FqWn230mtB.J0V2C2-jJbllb47r
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 00:51 Hello, hello alone.
**Pierre Tessier** 00:56 Ayy.
**Juliano Costa | Datadog** 00:59 Oh… Where are you?
**Pierre Tessier** 01:02 Getting busy with work.
**Juliano Costa | Datadog** 01:08 Man, I…
**Pierre Tessier** 01:09 They just got back, so… which is good, I guess.
**Juliano Costa | Datadog** 01:14 I… I didn't realize, but when I saw your… I saw a post from you on LinkedIn, and I was reading, like, with my Brazilian head.
And the company that you work for, it's called Resolve AI, but if you… if you speak in Portuguese, it's like… it would be, like, something like, something that we would say whenever someone is, like, how can I explain that now? So, when you did a mess, and then it would just go to that person and say… to the person that did the mass, and then you say, hey.
So that, like, Fix this, like… Because… I, or, well, in English it's AI, but I in Portuguese is, like, there, or… .
**Pierre Tessier** 02:18 Yeah.
**Juliano Costa | Datadog** 02:19 So, kind of fix this. But it kind of works for, for your, for your…
**Pierre Tessier** 02:25 It does work.
**Juliano Costa | Datadog** 02:25 company's case, yeah, but it's funny, and I was… I guess with resilience will be funnier, but yeah.
At least it was funnier on my head, so, yeah, nice.
Good job, Julian.
Okay, so… I… I've been fighting with, Copilot for a while today, so this is… this is fun. Like, I… I raised up PR.
And… Peter, asked Copilot to review.
And then the change that was, like, 4 lines became 69 lines, because Copilot keeps pushing, and Cloud keeps, like, fixing whatever, Copilot says, so yeah, I'm, like, back and forth with them, and just wishing to… Please, can you just leave me alone?
That's, that's related to an issue that I have… that we have, actually, on the… On the front-end proxy, the… theologian.
It's calling… the playwright is calling a service, and when the image is not loaded, it calls undefined.
So I was getting a bunch of 400, And I was like, huh, from where this is coming from? Then, Claude did some digging for me, and, yeah, It solved. You are on mute, Pierre.
**Pierre Tessier** 04:22 So the issue was the load generator was just calling something wrong?
**Juliano Costa | Datadog** 04:26 No, load generator is calling, correctly, and Playwright is also configured correctly. The problem is front-end, so… I have a description of the issue here, adding to the doc.
**Donal O'Sullivan** 04:44 Is it… it's probably a timing issue, is it? So, when Playwright makes the call, the image hasn't been loaded yet, I guess, is it?
**Juliano Costa | Datadog** 04:55 So, yeah, whenever a product is rendered without a picture, in the API response?
then the front-end proxy logs, like, get images, products, undefined. Well, it doesn't log, it actually queries that, and as this is an invalid URL, then I get a 404.
**Donal O'Sullivan** 05:17 Yeah, yeah. But it just could be that it hasn't rendered yet. Do you know, Playwright is making a call before it's actually finished?
**Juliano Costa | Datadog** 05:27 Yeah, but I… that was my initial… thought to fix, so I said, hey, can we configure Playwright to wait for that?
And, Claude actually told me that the ideal solution would be to fix on the front-end side, and that's why, like, the changes are on the front end.
So it's touching product card, cart items, cart drop-down, checkout, And, Pages product.
So, yeah, And, I think… Jonathan, did you raise a PR, or did I see something from you? Yes, I did. Yeah, there you go.
Yeah, I had a crazy…
**Jonathan Munz** 06:25 Things to the agenda.
**Juliano Costa | Datadog** 06:27 Ako, okay.
We have the support for Podman, that… Donald, raised.
Are the changes too… too big to… to that?
**Donal O'Sullivan** 06:49 So… Yeah, this was just to kind of ask the question, I was able to… I'm able to get it running locally with Makestart using Podman, there's just a few changes that have to be done.
The biggest one, I think it's in the actual GitHub issue, but… So the biggest change was literally… it was updating… sorry, let me open the GitHub issue there. So in the, Docker Compose file, we use a tag for the service name.
And we have to remove that. And once we remove that, it's fairly, like, it's very straightforward. It will just work, kind of, out of the box.
**Pierre Tessier** 07:32 Is that just because Podman just doesn't support tag for, log definitions?
**Donal O'Sullivan** 07:37 Yeah, that's what it looks like. If you look at the log, like, the actual… under the hood logs, it's complaining about tags, so you just remove it, and it just works.
Bit annoying, but…
**Pierre Tessier** 07:48 Part of me wants to say, shouldn't Podman support that, even if it does nothing with it?
Because it's part of the Docker Compose spec, and they were supposed to be… I'll deal with that.
**Donal O'Sullivan** 07:57 Like, yeah, that's true, yeah, yeah.
**Pierre Tessier** 07:59 So, part of me wants to say, should we not be raising an issue?
with Podman about this?
**Donal O'Sullivan** 08:08 Yeah, that's… yeah, that's good shows. Good luck.
**Pierre Tessier** 08:11 Oh.
**Donal O'Sullivan** 08:11 Yeah.
**Pierre Tessier** 08:12 Because, you know, like, it's supposed to work, and it doesn't work. It's probably one of the great things about the demo, is we get to find out all the things that are supposed to work that actually don't.
Because… reasons, right? Software is complicated.
I think, hey, let's do this, because we don't use it anyways, right? So let's go ahead and make that, but I think at the same time, you know, being good OSS citizens, we should raise this flag with Podman and say, yo, you're supposed to support this, but you don't. It's broken, maybe I have the support.
But yeah, that's just me being, I don't know.
It's supposed to work, so…
**Donal O'Sullivan** 08:49 Yeah, no, no, it's a good shout, yeah, because it is annoying that you have to, like, remove that, just to get Pod Mentor on, because if you leave it there, and you do make start, it just crashes, and then it can… you look at the journal logs, and it just says, Yes, there's just, like, an error around that tag. So, are we using that tag at the moment in Docker Compose? Is it actively used, or…
**Pierre Tessier** 09:11 It shows up when you do, like, Docker logs, yeah.
**Donal O'Sullivan** 09:16 Yeah.
**Pierre Tessier** 09:16 Because it's coming from all the services. Honestly, I don't know anybody who would do that at this point today.
Because we're pretty noisy now, right? And it's hard to look at all the logs across all… you'll probably focus on one service at a time. Yeah. But, you know, early days, when we first started doing this, and there was very little telemetry emitted from everything.
It made sense. Today, probably not so much.
**Donal O'Sullivan** 09:47 Okay, cool.
**Pierre Tessier** 09:48 but yeah, we should, you know… Juliana, unless somebody else has an objection, we should probably just remove tag.
From our logs.
**Juliano Costa | Datadog** 09:59 Yeah, happy to. Well, actually, I would even suggest having Podman as the… No, no, that… I think that would be too big of a breaking change.
**Pierre Tessier** 10:14 You know, I think if somebody wants to run Padme, they could do their own thing, right? They just have a couple environment variables and are off to the races, right?
**Juliano Costa | Datadog** 10:22 Yeah, it's just that, Podman is now a Linux Foundation project. Yeah.
**Donal O'Sullivan** 10:28 CNC.
**Juliano Costa | Datadog** 10:28 Oh.
**Donal O'Sullivan** 10:29 Yeah.
I… I can open a PR just to show, like, a demonstration of how I run it with Podmen, like, it's… there's very little changes, it's literally just getting rid of that tag, and I think I just changed, like, the socket path or something like that. And if that… if that works, like, you guys can have a look and see what I've done, and go from there, maybe.
**Juliano Costa | Datadog** 10:51 Yep, sounds good.
**Pierre Tessier** 10:52 Yeah, you just changed the… Yeah, Potterman Compose… and the… You know, if anything, it probably wouldn't hurt to have a doc.
For this, for people who want to use Podman.
**Donal O'Sullivan** 11:08 Yep.
**Pierre Tessier** 11:09 As well.
You know, PR first, to remove this thing, just to validate it all works, and we should probably add a doc entry, you know, to how to run the demo, and getting started, whatever it is, and one of them should just be, Podman.
**Donal O'Sullivan** 11:22 Yep.
I can… Yeah, I can do that.
So are we saying 1PR to literally just remove tag, then? Is that it?
Okay. Okay, cool.
Makes sense. Alright, yeah, I can do that. So, PR to remove tag, maybe another draft PR, just to show how I'm using Podman to run the demo, and then, yeah, documentation update.
Hmm.
**Juliano Costa | Datadog** 11:47 I think that the second one we can already raise on the OpenTelemptory.io.
like, as a… and if you navigate to the deploy the demo, you have Docker, Kubernetes.
**Donal O'Sullivan** 12:03 Cheers.
**Juliano Costa | Datadog** 12:03 And maybe we can just create another option, Podman, and then I'll have these steps there. I think that would be a nice addition.
**Donal O'Sullivan** 12:12 Cool. Yeah, no, I like… yeah, I actually like the sound… that sounds good, I like the sound of that. Cool, okay.
**Juliano Costa | Datadog** 12:18 Quick question for you, I don't know if you have tested, but do you know if the Docker receiver, the Docker metrics receiver, works with Podman?
**Donal O'Sullivan** 12:27 So Docker Stats, is it?
**Juliano Costa | Datadog** 12:30 Yup.
**Donal O'Sullivan** 12:31 Yeah, I think it does… yeah, so it does… as far as I could tell, it works. There is a Podman Stats receiver as well.
I think… but I think, yeah, because Podman and Dock… you know, Podman is supposed to basically work the same as Docker, I think the.
locker stats one seems to work, and I know I checked Grafana and all the… all the dashboards, they did seem to work. I'll double-check that, though, just… just to confirm.
**Juliano Costa | Datadog** 12:55 Okay, sounds cool. Because then, if it doesn't work, and we have a podman receiver, maybe we could add to the docs as well, like, hey, Swap those components.
Yeah. Just…
**Donal O'Sullivan** 13:09 Yeah.
**Juliano Costa | Datadog** 13:09 Just so people have the same complete experience in both scenarios.
**Donal O'Sullivan** 13:14 Makes sense.
Cool.
**Juliano Costa | Datadog** 13:16 Nice. Cool.
**Donal O'Sullivan** 13:20 Thanks, guys.
**Juliano Costa | Datadog** 13:22 Thank you.
**Pierre Tessier** 13:25 Alright.
**Juliano Costa | Datadog** 13:27 Jonathan, the stage is yours. I love the PR, by the way, like, minus… 19 lines plus 7. Perfect. Minus 19,000 lines, yes.
**Jonathan Munz** 13:41 Well, I guess I was the one who added those 19,000 in the first place, so I'm just cleaning up. But yeah, this is just following up from last… so… The original goal was the… bumped to the latest expo… React Native, so that's… that's the change, why there's so many deletions. I think that this was true of… the version when I originally put the React Native app, but I think, This system is more, robust now, but basically.
the best practices for Expo, now is to not actually version control the Android and iOS native folders that are needed for the app.
but to have those be generated on the fly. So, that's the other half of that PR, is as part of going to the latest expo, nuke those folders, and And now, when you create the React Native app, when you run it, it will create them. But they won't be version controlled, so that helps.
what… with what originally precipitated this was trying to update the Gradle version in that native Android folder. That will just be… They'll just be transitive now, based on whatever it needs to run the app.
So the PR looks large, but it's mostly getting rid of those Android and iOS folders, and then the package lock file obviously had a huge number of changes, but It's probably ready to look at, I still need to… I just did the most basic verification of… launching it on Android and seeing it worked, I didn't do iOS, I didn't look at the, building the APK through the Docker thing, so those are the next things I'll need to do, and I think there's a couple failing checks that I need to look at.
To… before that's ready for, for merge.
**Juliano Costa | Datadog** 15:34 Oh, do you have, Are you able to test the iOS part as well, or did…
**Jonathan Munz** 15:42 Yeah, I just haven't gotten to it yet. Yeah, I think I should be able to test the remainder, but yeah, I just didn't get to it.
Yeah. Yeah, it was a lot of red, so it was nice.
Cool, and the second one there was just something I noted when getting it, so, I don't know if you all want that as a separate PR, but there is a typo in the Docker minimal.
That was making me… that failed this… I wasn't able to run start minimal because of that. It fixed directly on that branch, but it's not really related.
And then just in general, I don't know if this is a me thing or… but I… I commented out open search and shipping entirely, because it… the demo wasn't running, for me with Start Minimal.
Put those there, so, I don't know if that's a.
**Juliano Costa | Datadog** 16:31 Okay.
**Jonathan Munz** 16:31 Another issue, or just something with my environment.
**Shenoy Pratik Gurudatt** 16:35 Please take a look at that.
**Pierre Tessier** 16:38 It could be a resource issue, because open search is pretty big, requires a lot of RAM.
**Jonathan Munz** 16:43 Possibly. Yeah, it seemed like it was start… it just kept… It was, like, healthy.
But it didn't last longer than 30 sec- like, every time I look at Dr. PS, it was, like, health… starting healthy 30 seconds ago, and, like, it never lasted longer than that, so something was killing it post-launch.
**Pierre Tessier** 17:01 open source.
**Jonathan Munz** 17:02 search was, like, consistently unhealthy. Sorry, reverse that. Shipping was consistently unhealthy. Open search was healthy, but kept restarting.
**Pierre Tessier** 17:13 I don't think I…
**Jonathan Munz** 17:15 I didn't try not minimal. This was only start minimal, so it might be something related to minimal.
**Pierre Tessier** 17:20 Okay.
Shipping depends on quote, and quote's not part of minimal. We should double check that.
**Donal O'Sullivan** 17:31 If it keeps restarting, it's probably, like, was it in Kubernetes that it was doing this?
**Jonathan Munz** 17:37 No, this is just straight… Running.
**Donal O'Sullivan** 17:40 Was this Docker, was this? Yeah.
It's probably just running…
**Jonathan Munz** 17:44 Kalima, technically, but yeah, it was just Rocky.
**Donal O'Sullivan** 17:46 Just a resource, like, it just keeps going out of memory, and then starts again, then…
**Jonathan Munz** 17:52 Possibly. I don't think I configured too many… too much there. Like, I've been able to start minimal in the past. I usually avoid the full start, so yeah, I haven't provisioned Locally for a ton of resources, so it's entirely possible.
**Donal O'Sullivan** 18:07 Okay.
**Jonathan Munz** 18:09 I was gonna mention, I don't know, maybe a separate issue, but just for the first one, for the typo, I think this is relevant for the podmin as well. I don't know if there's some… sort of… smoke test we can add to the CI to just… like, Docker Compose start with start, Docker Compose would start minimal, podMen for both, just to see that… it gets… I don't think it would catch something like I'm saying with the open search restarting, but it would at least catch, like, something like the typo, or something like the tag… if someone added tags back to the Docker file at some point, that would make Podmen stop working again.
**Juliano Costa | Datadog** 18:50 Aye.
Yeah, I would actually love to have, some sort of… proper validation from our end on the PRs itself. I think we were discussing that, last week, and PR had a Jaeger Tracer validator, but the Jaeger Tracer validator wouldn't validate logs and metrics.
So…
**Jonathan Munz** 19:15 Well, I wonder if they're simpler… I don't know if Docker or Podman have a mode like this, but is there a way to run them such that they don't even build the containers, but that they're just flagged that they're happy with… the files? Like, the Compose syntax?
**Juliano Costa | Datadog** 19:29 So, kind of, validate… Validate YAML.
**Jonathan Munz** 19:34 Yeah.
**Juliano Costa | Datadog** 19:35 Yeah, but then that wouldn't solve the… I mean, it would cover one thing, but yeah.
**Jonathan Munz** 19:41 Yeah, we cover some of this, but yeah, not all.
**Donal O'Sullivan** 19:46 It's like a… it's a…
**Pierre Tessier** 19:47 I couldn't even figure out.
**Donal O'Sullivan** 19:47 Sorry, go ahead.
**Pierre Tessier** 19:55 That was probably me that added that by accident in a PR a couple weeks ago, right? Or last week?
And that's why it was missed?
**Juliano Costa | Datadog** 20:05 W-what?
**Pierre Tessier** 20:08 No, because I was doing that as part of my compose layers.
Oh.
Yeah, I'm trying to figure out how this got… how this got inserted and not caught before.
we should have caught this, it was like, you know.
when we would emerge the PRs, so… Because that's a syntax error for Docker Compose. It shouldn't have never made it through for… you know.
**Juliano Costa | Datadog** 20:42 S… As we are talking about, Jesus.
As we were talking about, open search.
I want to share this with you all.
I have… I'm running the demo locally.
I'm getting a bunch of those things here. Are you guys also getting this?
So… this is a… On the open search, it's dropping items.
I do… I think… That has something to do with resource.
mapping, or…
**Shenoy Pratik Gurudatt** 21:35 Yeah, this is a common issue, where if you have Something like an object field, but it was injected as a string earlier.
And now you have a child of that string… string field coming in, and open search, it's, confused, thinking that it's… it should be a string, because there was a string object that came in earlier, but now it's coming in as object.
So…
**Juliano Costa | Datadog** 22:01 Okay.
**Shenoy Pratik Gurudatt** 22:01 But… that's the issue.
Ideally, we fix the instrumentation side, and make sure if you have something like a source.address sending out a string from one service, it should be string for all the services. It shouldn't be an object for any other service. I can… Okay, so if you have your exact log clients, I can go and fix them in the instrumentation side.
**Juliano Costa | Datadog** 22:22 This is actually good. I love when we find those things on the demo.
**Shenoy Pratik Gurudatt** 22:27 Yeah, this is something that we found with Viewer as well, when we were adding docs. Yeah.
If this is something we can fix at instrumentation.
**Juliano Costa | Datadog** 22:38 I will add, I'm creating an issue, and I'll add this log here.
**Shenoy Pratik Gurudatt** 22:46 Yeah, you can assign it to me, I can fix them. And if you see any more of them, just add it to the same issue. I have seen them a couple of times. It's time to…
**Juliano Costa | Datadog** 23:10 Cool.
**Shenoy Pratik Gurudatt** 23:12 And for the restart issue, Pia, I know you were mentioning about the trace testing that you're working on.
So with the Jaeger traces, can we also… I, like, I can, work with you to add some testing for open source logs, for example.
Or check even Prometheus to see that things are going on fine.
**Pierre Tessier** 23:31 That's what I'm starting to think, now that we just mentioned it, it's… we should just test Jager, we should also be testing OpenSearch and Prometheus to query metrics blogs.
associated with each one as well. Metrics, I think, should always be on. Oh, no, I mean, because we have custom metrics as well that we want to check. The other point with metrics, though, is that they take a minute plus to emit.
which would cause delays in RCI.
Which… I guess, fine, but…
**Shenoy Pratik Gurudatt** 24:06 I think a minute or two is fine.
**Pierre Tessier** 24:08 Yeah.
**Juliano Costa | Datadog** 24:09 Yeah, I…
**Shenoy Pratik Gurudatt** 24:09 Validate things are working.
**Pierre Tessier** 24:11 As long as it's not 30 minutes like it was before with trace testing. That was a big thing we had a problem with trace testing, is that it would take up to 30 minutes for it to do a cycle, and it would… you know, you're trying to merge PRs, and you're waiting for it to finish.
**Juliano Costa | Datadog** 24:24 But if we, with the current setup, we can just add, like, merge to… Add to the queue merge, merge queue, whatever, and then, like, if it fails, then… the problem of trace tests was that it was flaky.
So… Sometimes it failed, we just, like, 15 minutes, failed, we restarted, 15 minutes, passed.
We're like, okay, yeah, great.
So, if it takes 15 minutes, but it's reliable, then we can just add to the merge queue and forget it.
And then we just come back to the ones that really crash, and then are not merged, because our CI is actually doing some validation.
**Pierre Tessier** 25:12 I think this changes a little bit of how we do things.
on this validator that I was building out, because it was really focused on just tracing.
**Juliano Costa | Datadog** 25:23 racing.
**Pierre Tessier** 25:24 Which is, you know, you emit a trace, wait a couple seconds, go check Jaeger for it.
This is now going to be a minute trace, wait a couple seconds, check Jaeger, check Open Search, and check a metric a minute later.
You know, so it feels like I have to… it blew up the scope of what I was just thinking of, and what I have, and what I need to finish cleaning up. I'm sorry I did not clean it up over the weekend. We had some family issues. My son had, some health things that we had to take care of, but, And… I used to open up a draft PR so we could start noodling on this together, and maybe we could collaborate on that. Would that help?
**Shenoy Pratik Gurudatt** 26:03 Yeah, yeah, yeah, that would definitely.
**Pierre Tessier** 26:04 Let me do that, no. So, it's… right now, it's all Python.
Python's easy to read, it's easy to do this kind of stuff in. So, I'll get the draft PR going.
Let's put it out there. I'm gonna rename a few things, because it makes more sense now, and we'll just call it, like, full-blown demo CI testing, or something like that. And, yeah, we should be testing open search. We should be testing metrics as well.
Oh, okay.
Can't wait for profiles.
**Juliano Costa | Datadog** 26:39 Talking about that, we still have 4 minutes. Donald, I tagged you, and I saw that you saw the message. Can we maybe have the dev filter as a container? I saw… I took a look at the wrap-up, and there was no thinner way of running, so I don't know if it's possible.
**Donal O'Sullivan** 27:01 You're talking about DevFiler, is it the desktop application?
**Juliano Costa | Datadog** 27:07 Yes, exactly. So…
**Donal O'Sullivan** 27:09 Yeah.
**Juliano Costa | Datadog** 27:09 We need, like, it's not about just adding profiling to the demo, we need.
**Donal O'Sullivan** 27:14 Yeah, yeah.
**Juliano Costa | Datadog** 27:14 We needed to see it, and I don't think there is an open source one, so…
**Donal O'Sullivan** 27:19 Oh, I know that.
**Juliano Costa | Datadog** 27:20 created this one that, you announced at KubeCon, so that would be.
**Donal O'Sullivan** 27:24 Yeah, so… Yeah, no, no, it's a good show. So there's just a couple things there. So the dev filer is mainly, like, for local desktop.
So, like, dev work locally, and you have it on your, you know, you have it running on your machine.
At Elastic, we do have, like, a universal profiler for Cabana, where we can view profiling, so we just send our profiling data to Elasticsearch, and we can, like.
view it that way. This is something I'm gonna… I'm looking to work out for our own fork of the demo.
regarding, you know, obviously this upstream demo, I was thinking, like, is there… there might be a backend we could use specifically for profiling, and use that to show it, potentially?
Because I just don't know if DevFiler is going to work that way, if that makes sense.
**Juliano Costa | Datadog** 28:15 I'm a bit hesitant to use a vendor solution on the demo.
**Donal O'Sullivan** 28:21 Hmm.
They're trying to do support profiling, don't they?
**Juliano Costa | Datadog** 28:29 equals.
**Donal O'Sullivan** 28:30 Boom.
**Juliano Costa | Datadog** 28:31 You are on… on mute, Pierre.
Are you still on mute? Yeah, yeah.
**Pierre Tessier** 28:37 Sorry. I… yeah, we… Ideally, it's open source, and it's part of the whole… Look, it's a free profiler, right? I know Pyroscope used to be there, but I don't think it's the same anymore.
**Juliano Costa | Datadog** 28:58 I think Parka supports hotel, profiles, but I don't think also Parka is open source, and…
**Donal O'Sullivan** 29:06 Hmm, yeah, yeah, yeah, okay.
**Juliano Costa | Datadog** 29:09 Or, if they are open source, they… they are a vendor as well, so it's like Grafana, open source, but they have their pain.
**Donal O'Sullivan** 29:18 Yeah, yeah.
**Juliano Costa | Datadog** 29:19 tier.
**Pierre Tessier** 29:23 Okay.
**Juliano Costa | Datadog** 29:24 I don't know.
**Pierre Tessier** 29:26 The slightly related profiles versus "-F.
Do we want to go forward with that dash FPR?
**Juliano Costa | Datadog** 29:36 I need to… I… I didn't have the time to take a look at that. Sorry.
**Pierre Tessier** 29:41 I'll hold off on it for now. Okay, fair enough. I know, I know, I know. We both said we were gonna do things we didn't do.
**Donal O'Sullivan** 29:53 Juliano, regarding the profile, and I can take that as an action, I can look into it more, and I can try and come back with some… with some different things, if that works for you.
**Juliano Costa | Datadog** 30:03 Cool, yeah, let's brainstorm, like, I… and I don't want to be bossy, saying, hey, no, like, if we agree that, Elastic is a good solution, let's set. It's just that… Yeah.
Yeah, I don't know. I don't know, let's discuss.
**Donal O'Sullivan** 30:25 No, I getcha, I getcha. I'll see what's out there, and I'll see if I can find something.
Cool.
**Juliano Costa | Datadog** 30:31 I got a drop, thanks, everyone, for joining. Shano, I sent you the issue that I just created.
**Shenoy Pratik Gurudatt** 30:39 Perfect, yep. I'll look into it and have something by next week.
**Juliano Costa | Datadog** 30:43 Awesome.
Cheers.
**Shenoy Pratik Gurudatt** 30:45 Thanks.
**Donal O'Sullivan** 30:46 You guys.
