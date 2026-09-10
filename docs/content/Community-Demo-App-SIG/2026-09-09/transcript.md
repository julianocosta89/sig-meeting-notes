SIG: Community Demo App SIG
Date: 2026-09-09
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Tobias Oka** 00:20 Hello there.
**Donal O'Sullivan** 00:27 Lowe.
**Tobias Oka** 00:30 Donal. How you doing?
**Donal O'Sullivan** 00:32 Let's about yourself.
**Tobias Oka** 00:34 Yeah.
Doing alright.
or as I would say to my colleagues, can't complain, because, you know, there's this German culture thing where… I mean, I guess maybe you also have that, like, where you say, not saying something bad is something good.
**Donal O'Sullivan** 00:53 Yeah, yeah, yeah.
You're… you're based in Germany, Tobias, are you?
**Tobias Oka** 01:00 I'm based out of Switzerland, but I did grow up in Germany, so…
**Donal O'Sullivan** 01:04 Cool.
**Tobias Oka** 01:06 Haven't fully, become… This… the kind of… you know.
Neutral, cushioning every statement that, that… That some people here like to do. I'm still a bit too blunt sometimes.
**Donal O'Sullivan** 01:25 I know, it's all good. There's no worries.
No worries.
Whereabouts in Switzerland are you based?
**Tobias Oka** 01:35 Zurich.
**Donal O'Sullivan** 01:36 Zurich, okay, yeah, yeah.
**Tobias Oka** 01:38 How about yourself? Where are you based?
**Donal O'Sullivan** 01:40 I live in Limerick, Ireland, so the west coast of Ireland, kind of like the Midwest.
**Tobias Oka** 01:46 I have seen it on the map, I've not been there myself. I've been to Dublin… I've been to… some values and places whose names I don't remember.
**Donal O'Sullivan** 01:58 Are you Wicklow, is it? Wicklow Mountains?
Oh.
**Tobias Oka** 02:01 That might be… I'm not very good with names. It was… very… like, the air… just… was… it felt like it was so clean, like, there was a lot of humidity in the air, it was, like, raining the whole time, but… Like, it just felt so fresh.
**Donal O'Sullivan** 02:23 Yeah, a lot of… a lot of foreigners say that. I know a lot of, my university, any Indian person I met, they would always say, like, the air is so clean.
Oh my god.
**Tobias Oka** 02:35 Oh, yeah, I mean, compared to… compared to some places in India, I've been to,
**Donal O'Sullivan** 02:41 Probably not her.
**Tobias Oka** 02:42 It's a very, very big difference, yeah. I would also say… so, I've been to Beijing a couple years ago in winter, and I don't know if that's still the case, but they used to heat a lot with coal.
And so, the air was really bad, so bad that I have never seen such bad air in Europe ever.
**Donal O'Sullivan** 03:00 Yeah, yeah, yeah, yeah.
But, so, Switzerland's good, like, I was there recently, I was in, I actually went to Lake Oshingen, probably familiar with it.
**Tobias Oka** 03:13 No, I'm not, actually, but there are so many lakes.
**Donal O'Sullivan** 03:17 It's, it's spectacular, like, it's, like, the… you basically… I think is it, like… It's very high up anyway, it's a couple thousand meters above sea level, and it's a big and you can hike around it, but yeah, like, the air was… air was very fresh, you know, it's just a… Very scenic, really nice lake.
**Tobias Oka** 03:37 Nice.
**Donal O'Sullivan** 03:38 Yeah, yeah.
**Tobias Oka** 03:39 I'm just trying to find it on…
**Donal O'Sullivan** 03:42 I'll get a…
**Tobias Oka** 03:43 maps…
**Donal O'Sullivan** 03:44 Pushing it.
I'm probably not even seeing it, Reef, yeah.
I'll put it in the, in the, in the chat.
**Tobias Oka** 04:00 Let's see, okay, yeah, I mean, I haven't been there.
**Donal O'Sullivan** 04:04 Yeah.
I'd recommend it, it's, like, real picturesque Switzerland. It's like the… when you think of Switzerland on a postcard, it's like, that's what you think of, you know?
**Tobias Oka** 04:15 Yeah. Like, green, rocky meadows, some spare, like, like, some trees, not a lot of foliage, and then, like, the…
**Donal O'Sullivan** 04:26 Yeah, yeah.
**Tobias Oka** 04:27 Snowy mountaintops.
**Donal O'Sullivan** 04:28 Yeah, yeah, real, real alpine, real alpine.
**Tobias Oka** 04:31 Yes.
**Donal O'Sullivan** 04:32 Yeah, yeah, yeah, yeah, it's cool. Yeah, I think it's a ski resort in the winter, but yeah.
**Tobias Oka** 04:41 I'm curious if the others are gonna join.
**Donal O'Sullivan** 04:45 King Juliano.
**Tobias Oka** 04:46 I was.
**Donal O'Sullivan** 04:47 Wow.
Usually, he joins everyone. He's online anyway, so… Let's give it a few more minutes.
Maybe if no one else joins, might just… Let me just call it a day.
**Tobias Oka** 05:06 I mean, if, like, while everyone's waiting, I mean, I joined the call two weeks ago, and I was presenting this this, PR, you know, this idea to take out the, kind of.
hardwired SDK dependency, and then wired it into the… the image instead. Have you, by any chance, had a chance to look at that and think about And maybe a test, if that… if that looks good.
**Donal O'Sullivan** 05:40 I haven't had a chance to hugely look at it. I think it does make sense, though, like, and like what you were saying, like, it… you can overwrite it. So, like, if you don't provide a value, it will take the value that's in the Dockerfile, but you can overwrite it then if you want to, so I don't… I wouldn't see an issue with it, per se.
Yeah, so it should be fine. I just need to check the, What service are you making the changes to again?
**Tobias Oka** 06:06 It is the payment service, and now I had to even think myself which one it was.
**Donal O'Sullivan** 06:11 Yeah.
Do you… yeah, like, I'm sure it's fine. I guess you'd be doing it from… You'd end up… we'd end up doing it for all the other services, is that the idea?
**Tobias Oka** 06:23 That's the idea, so this is kind of a prototype so far, doing it with one service, and… if it's good, like, I would do it with the ones where it can be done, right? So we can only do it for those where we actually have this runtime instrumentation capability.
**Donal O'Sullivan** 06:41 Yep, yep.
Yeah, yeah, agreed, yeah, yeah, makes sense. Yeah, do you want to put the… the pull request in the meeting notes for today, just so that we have a… Oh my god.
**Tobias Oka** 06:55 I mean, I'm… let me see where I have the meeting notes. I put it in the chat for now.
It should… oh, it's…
**Donal O'Sullivan** 07:00 Is it in the Slack thread, is it?
You put it in the, just for today's agenda, but just the mark that we spoke about.
**Tobias Oka** 07:09 Meeting notes, there it is, okay.
Yeah.
**Donal O'Sullivan** 07:13 Many of the maintainers.
didn't join the call, they could just look at what was discussed, like, it might just be, like, review this PR or something like that.
Just as a reminder.
**Tobias Oka** 07:23 Yep. Okay, so let me… Probably even add this date tag, I have no idea how we even add this. Maybe I just duplicate it and then changed the date?
**Donal O'Sullivan** 07:35 Nope.
**Tobias Oka** 07:36 I don't think.
**Donal O'Sullivan** 07:36 You just do… no, just do at today.
**Tobias Oka** 07:40 Oh, and today… Okay.
**Donal O'Sullivan** 07:44 There you go.
**Tobias Oka** 07:45 Learning something, you know.
**Donal O'Sullivan** 07:46 Alright, hang on. Oh, yeah, to that, yeah, that's right, 9-9, yeah.
Cool.
**Tobias Oka** 07:52 And then I copy the structure, so we have…
**Juliano Costa | Datadog** 07:58 hurry.
**Tobias Oka** 07:59 In terms of attendees… Hey!
**Donal O'Sullivan** 08:03 below it.
**Tobias Oka** 08:03 Hi, Dune.
**Juliano Costa | Datadog** 08:05 Yeah, bye.
Yeah, I'm stressed.
Next, next week, next Tuesday is the Datadog Summit Sao Paulo, and I'm taking care of the whole, agenda, so, yeah. I was just in a call with a customer.
Sorry.
**Donal O'Sullivan** 08:26 Are you… are you going? Is that an event? Are you going to it?
**Juliano Costa | Datadog** 08:30 Yeah, it is an event, a Datadog event where customers present, so… Yeah, and I'm the only one on my team that speaks Portuguese, so…
**Donal O'Sullivan** 08:41 They are.
**Juliano Costa | Datadog** 08:42 Sending me there.
**Donal O'Sullivan** 08:44 Nice.
**Juliano Costa | Datadog** 08:46 Yeah, it's cool to get a trip to Brazil, but yeah.
**Donal O'Sullivan** 08:51 I was just gonna say it, how bad?
Very good.
**Juliano Costa | Datadog** 08:59 Donal, I was talking with Tobias, Tobias.
I know, like, the Portuguese way of saying Tobias is Tobias, so I'm always confused, sorry.
**Tobias Oka** 09:11 Which is also the way they would say it in German, so, you know…
**Juliano Costa | Datadog** 09:14 Oh, okay.
Perfect.
**Tobias Oka** 09:17 Yeah, Donal and I had already had a short conversation, actually. Cool.
**Juliano Costa | Datadog** 09:23 Perfect.
We need… By the way, I need to cut a release because of the CAIC thing.
**Donal O'Sullivan** 09:33 Yeah.
**Juliano Costa | Datadog** 09:34 It was just… maybe we can also have that on the release, so then 3.1 already has the… Disney.
**Donal O'Sullivan** 09:46 Yeah, yeah, sounds good. Yeah, yeah, it sounds good to me.
Yeah, I'll just quickly check the PR, If not this evening, it'll be tomorrow morning. But yeah, it sounds fine.
**Juliano Costa | Datadog** 10:03 Okay.
No worries.
On other front, the… purses… thingy.
So, the, the PR… the, the, the… one of the maintainers from Persys opened. They had the exemplars dashboard, but Persys do not support exemplars yet.
**Donal O'Sullivan** 10:28 Yeah.
**Juliano Costa | Datadog** 10:29 So what I did was, I was like, hey, I never, checked purses before, maybe I can put my bots to work on that. So, I actually opened 4 PRs, got one merged already, so I'm waiting, 3 other PRs, and that actually adds, exemplars to purses. So then, if we get that, then we can, merge back. I think.
**Donal O'Sullivan** 10:54 Interesting.
**Juliano Costa | Datadog** 10:55 It may take a while, because, like, I'm adding the… I mean, adding the support so we can see exemplars, but I think I need to elaborate a little bit more on, cross-plugings thing is, like, cross-pluggings linking, because exemplars is Prometheus.
And in metrics, and then when the user clicks, it opens the pop-up with the trace ID and stuff. So, ideally, at least in my opinion, if I have a trace ID and I have Jaeger plugin also enabled, I should be able to navigate from the from the metric to the trace, and not just copy the trace ID, go to Jaeger, and then paste the trace ID, which would be, like…
**Donal O'Sullivan** 11:43 Hmm.
**Juliano Costa | Datadog** 11:43 not a good experience. So that may take a while to land, but just so you know, it's, moving, so… Yeah, yeah.
**Donal O'Sullivan** 11:50 Okay, yeah, yeah, because the PR was closed, wasn't it?
Yeah. Yeah.
Yeah.
**Juliano Costa | Datadog** 11:56 Yeah, CJO mentioned, hey, we could have both, but then this is just, like, an extra thing that we need to maintain, and I don't know how much you open Grafana, but, like, the dashboards in Grafana are not… Not all working, so yeah, it's a bit…
**Donal O'Sullivan** 12:15 Yeah, yeah.
**Juliano Costa | Datadog** 12:17 a bit of a pain maintaining the tool that you do not work with, so…
**Donal O'Sullivan** 12:23 More of a resource burden as well, if you just run the full demo.
**Juliano Costa | Datadog** 12:27 Yeah.
Indeed, indeed.
Yeah, that… that's the only thing that I had on my… on my list. I don't think… do we have any…
**Donal O'Sullivan** 12:41 I see.
**Juliano Costa | Datadog** 12:41 that need a touch.
**Donal O'Sullivan** 12:43 I saw your feedback on the Podman fixes, so I… I have… so I updated the CI now to only run on changes to the Docker files, but I know, There was another comment as well, just around…
**Juliano Costa | Datadog** 13:00 the,
**Donal O'Sullivan** 13:01 So maybe Brent, like, take, yeah, take that out and put it into a separate PR, which makes sense, I think, and then have it on, like, and, like, block merges if the build fails.
If the build check fails, which is fine. So I'm, like, I'm happy with that, like, we can take out the CI checks into a different pull request and just merge the fixes first, and then… I can… I can work on that when I can, you know, on… on… I can add the CI step to run the Podman build, to make sure all the images build are Podman build, and then, yeah, I think… What was the other… the other request was for, Is it the test, so run it in, like, the build, the build test, or what is it? What's it called?
**Juliano Costa | Datadog** 13:44 my… my point was actually a bit different from… so, I'm taking a look at the PR here. My point was a bit different, actually.
**Donal O'Sullivan** 13:58 Okay.
**Juliano Costa | Datadog** 13:59 I think if you… I do not know by heart, but I think if we take a look at the other builds, what we have is, let's say that someone changes the accounting service.
**Donal O'Sullivan** 14:12 Yeah, yeah, yeah.
**Juliano Costa | Datadog** 14:13 We'll only build for the accounting service, not for all the services.
**Donal O'Sullivan** 14:17 Okay, I understand, I get what you're saying.
Yeah, yeah.
Yeah, I know what you mean. Like, the thing is… do we need to check if someone changes, for example, the accounting service, like, source code? Probably not. We only really need to check, like, if there's a change to the Docker file.
Because we already have build checks for Docker, which will check if, like, the code change will work, but, like.
I guess… Yeah, I'm just thinking… Thinking out loud. Yeah, maybe it's easier to just add a podman check as well.
I guess just for compatibility between Docker and Podman, like, Podman's just stricter with, like, the syntax, so, like, if you do certain… use certain syntax in the Docker files, you have to… you, you know, do it in a certain way, whereas Docker doesn't really care, So are you saying, like, any change at all to a service will trigger a build, say, for instance… I think it already does for Docker, but it'll do it for Podman as well, so if there's a code change on the accountant service, run the Podman check.
That's what you're saying.
**Juliano Costa | Datadog** 15:28 Yeah, I think, I think that would make more sense, but… I mean, we could be more… I think we can be more restrictive on deployment, because if it builds on Docker, which we are already testing, and we limit the test to whenever there is a change only on the Docker file.
**Donal O'Sullivan** 15:52 Yeah, yeah, yeah.
**Juliano Costa | Datadog** 15:53 And if the service changes, we will not test appointment, but if Dockerfile changes, then we will test both.
**Donal O'Sullivan** 16:00 Yep, yep.
Yeah, so that's what… so that's what I've done now. I've updated the PR, so the CI check now only runs on Dockerfile changes.
So… Yeah, well, I guess what you're saying is.
if it… if there's a Dockerfile change only for one service, only run the Podman check on that service, don't run, like, the full suite. So, yeah, so that makes sense. Yeah. So, how about I take those changes out of the PR altogether, and we'll just… I'll open in…
**Juliano Costa | Datadog** 16:30 Yep.
**Donal O'Sullivan** 16:30 They open a sub-issue, or maybe a new issue? Maybe a new issue, and just say, like, pod mem, get checks, I can describe what we've discussed here.
**Juliano Costa | Datadog** 16:38 Yeah, sounds good.
**Donal O'Sullivan** 16:40 Okay.
**Juliano Costa | Datadog** 16:40 Let's do that, because then we can get the appointment support back in.
**Donal O'Sullivan** 16:45 Yeah, yeah, cool, makes sense. Alright, next one.
**Juliano Costa | Datadog** 16:47 Awesome. And also, that won't… So the checks do not… Actually affect or impact the release.
Because this is just a pipeline, so once we have the pod man supporting, I can, release, and then we have the checks later that, like, it's not a blocker.
**Donal O'Sullivan** 17:10 Yeah, yeah, yeah, yeah, exactly, I getcha, makes sense. Okay, cool, I'll just make a note of that.
Long… Alright, cool.
I have nothing else, anyway, so… I'll take a look at your PR, so twice.
**Tobias Oka** 18:30 Yep.
And so I… I'm planning to join those calls a bit more often. Like, maybe, you know, this is not… Something super productive, or relevant here, but… I realized that, you know, like, in my everyday job, I'm so much… involved in… You know, kind of… customer conversations, which can be sometimes very dramatic, and somehow I find it very grounding to just talk about some tech stuff.
That is, you know, it's like… it's like my feet can't touch the ground, you know?
That makes sense.
**Juliano Costa | Datadog** 19:12 Yeah.
**Tobias Oka** 19:14 So, yeah, hoping to make some more contributions.
**Donal O'Sullivan** 19:19 Cool.
**Tobias Oka** 19:22 Right.
So if there's nothing else…
**Juliano Costa | Datadog** 19:29 Very good.
No, next week I'm in Brazil. I may be able to join, but I won't promise.
Yeah, no. Next week, I won't, because that's the day I'll be traveling to my hometown.
The other one I may be able to join.
**Donal O'Sullivan** 19:54 True.
**Juliano Costa | Datadog** 19:58 Cool. Okay.
**Donal O'Sullivan** 20:01 Officially.
**Tobias Oka** 20:02 Okay. How do you say that? Borg, or something like that.
**Juliano Costa | Datadog** 20:07 Exactly. That's it. Bonsai.
As you join me, we are leaving.
**Shenoy Pratik** 20:17 Sorry for the lingering.
**Juliano Costa | Datadog** 20:20 No worries.
So we, we, we discussed a couple of things, I think, priorities here.
is to… just to get you up to speed, take a look at Tobias PR. I think I tagged you in Donal a couple of days ago.
And I will cut a release, so I'll waive that, so I can, merge that PR, and then I'll cut a release because of the K6, Licensed thing.
**Shenoy Pratik** 20:56 Yep.
That makes sense.
**Juliano Costa | Datadog** 20:58 Ugh.
**Shenoy Pratik** 20:58 Yeah. I'm excited to use the changelog release. Let's see if it works or not.
**Juliano Costa | Datadog** 21:06 Okay, the instructions are on the contributing, right?
**Shenoy Pratik** 21:12 Yeah, yeah, yeah.
**Juliano Costa | Datadog** 21:13 Okay, yeah.
**Shenoy Pratik** 21:15 It'll work, it'll work. I did… I did try it out, so, yeah.
**Juliano Costa | Datadog** 21:20 Cool.
Well, okay.
**Shenoy Pratik** 21:23 Yeah.
**Juliano Costa | Datadog** 21:23 Provide feedback.
**Shenoy Pratik** 21:25 Yeah, I started looking into Tobias CPR. It, like, worked and everything looked good.
But I… let me try to see if I can check anything from the modification side, if there is any downstream SDK or something that people use. I can also take that view.
And then put it in.
**Tobias Oka** 21:45 And by the way, I did test the stuff that we discussed in Last… like, the two weeks ago.
Right? So… We don't… I… no, I didn't only validate that nothing gets… lost, no telemetry gets removed, it's also that nothing gets kind of duplicated.
And I've documented in the comments, like, so there are actually some small changes, like, actually, before my change, some logs were getting duplicated, and now they're not getting duplicated anymore, which I think is a net positive, but yeah.
It's this documented there.
**Juliano Costa | Datadog** 22:27 Awesome.
Okay.
Then, see you all in 2 weeks.
But, yeah, keep the demo moving forward. Go for it, guys.
**Donal O'Sullivan** 22:40 Sounds good. Best of luck in, in Brazil, Juliano.
**Juliano Costa | Datadog** 22:44 Thank you.
Cheers.
**Tobias Oka** 22:47 Peace.
