SIG: eBPF instrumentation
Date: 2025-10-22
Duration: 26 minutes
Zoom Recording URL: https://zoom.us/rec/share/CUExmrhsNNZ70MlLwrD8OU4sNJLnj_462EyaVC4poh1BI4rzGqpvE1eVQEFoB8HX.435543SatB1BH3ly
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 00:45 Hey.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 00:46 Dang.
**Tyler Yahn** 00:48 How's it going?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 00:50 Good, good to be back.
**Tyler Yahn** 00:52 Yeah.
**Giuseppe Ognibene | Coralogix** 00:53 It is…
**Tyler Yahn** 00:53 A lot of travel. Hey, Sebi.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 00:55 Okay.
**Tyler Yahn** 00:57 Hey, Steven.
**Stephen Lang** 00:58 Alright, good.
**Tyler Yahn** 01:52 So I'm just, finishing setting up over here. We could probably get started in just a little bit. If you have agenda items you wanted to talk about, please go ahead and add them to the agenda, and if you haven't already, please add yourself to the attendees list, and yeah, we'll jump in in just a second.
Nicola, is, Mario gonna be able to make it today?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 02:11 I think so, I haven't heard, Oh, actually, he… let me check, I think he did mention he's got a…
**Tyler Yahn** 02:19 Oh, okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 02:19 He might be late. Yeah, he might be late.
**Tyler Yahn** 02:23 Cool.
No worries.
Cool. Alright, well, let's, jump in here.
Awesome. So, Steven, you wanted to start us off by talking about Exporting integration test functions for usability?
**Stephen Lang** 02:52 Yeah, so, as you're aware, there's a fair amount of overlap between Obi and Baylor.
And as we're working upstream first.
all of the work for CI and the integration testing that I've been doing recently has been going straight into OBI.
Part of what I've been doing recently is trying to bring back some of that work into Baylor, which has worked fairly well to a point.
But one thing we have is a sort of a great difficulty in reusing the integration tests from OB.
And one of the reasons is that, the integration test functions themselves are unexported.
So I'm kind of wondering if, like.
So, a quick but selfish win would be to You know, just initial caps on some of these integration test functions.
not test, because we don't want to mess up the whole test framework such that GoTest picks up all of these new tests.
And does some kind of duplicate execution of these.
But, you know, for the sake of reusability.
for, projects that are using OB as a library.
You know, it might be a help.
For validation, if instead of, You know, duplicating the test functionality.
Some of these integration tests, or all of these integration test functions, could be exported.
So, yeah, that's what I wanted to, to see what… what people think about, about this.
**Tyler Yahn** 04:30 I mean, I think that sounds like a, totally… fine proposal, You need to make sure that whatever functions you need aren't in… Test files?
the API doesn't actually export them if they are, so even if you have, like, exported files and test files, like, they won't actually make it into the public API.
But yeah, I mean… Yeah, we do this a lot as well in, like, the Upstream Go repository.
Where we have, like, specific testing functions, or testing packages. So, thing that comes to mind is, like, a metric data test package, which tests the metric data package. So I don't know if there's, like, some sort of structure you wanted to build in that… that would follow that same pattern, but I think that seems reasonable. Yeah, the reusability isn't… I think it'd be helpful.
**Stephen Lang** 05:24 Yeah, I mean, you know, a separate kind of test package, which you mean would effectively then be imported into OB, as well as into any other downstream project. I mean, that sounds a bit nicer, a bit less hacky, a bit more intentional.
If, you know, if that kind of… I could look at, You know, putting something together for that.
**Tyler Yahn** 05:50 Yeah, the main idea is then you get nice isolation with all of your testing functionality. It also sometimes helps with, like, dependency cycles. There can be, like, some weird things if you try to, like… if you put it all in one package, then it doesn't matter, but if you try to, like, have these, like, things depend on each other, then it can get a little funky.
But, yeah, I think that's… it's always… it seems to work fine. It also can be kind of like a… I mean, it's very clear, because you can make package documentation say that it's a testing package.
it doesn't always follow a lot of, like, standards, namely that it imports, like, you know, testing things in its, in its argument list or something like that, but, like, yeah, I mean, I think that that's always a… pretty straightforward way to do it. I don't know how… much you need to refactor to make that happen, though, I guess is kind of the question.
**Stephen Lang** 06:39 Yeah, yeah, I mean, that would be something that I was thinking of, if I was going to go down this route, would be to Do, like, an incremental refactor.
Because some of the integration tests are way more involved than others, so I could look at the ones with fewer dependencies and start with those, and maybe try and… For example, I could create a new package, take some of the existing tests, and refactor them out to use that package instead.
And instead of trying to do everything all at once, could maybe piecemeal you know, move over to the new package for some of the functions in OB first.
I mean, that could even… maybe I could do an initial PR just to show what that would look like.
And then if all looks good.
You know, then it should be fairly straightforward just to… Refactor the rest of it from there.
**Tyler Yahn** 07:30 Yeah, I think that sounds like a great plan. I… I think it sounds perfect, yeah.
**Stephen Lang** 07:36 Awesome, great, okay, well, I'll take some time to, to have a look and maybe start the draft for, Where the initial part of the refactoring could take place.
**Tyler Yahn** 07:46 Yeah, okay, alright, well, keep an eye out for it.
**Stephen Lang** 07:50 Awesome.
**Tyler Yahn** 07:50 Yeah, thanks again.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:52 This is sort of related to the last item that we wanted to discuss, the milestone 0.1, because we have one issue remaining there.
That Mario did a bunch of work for.
I don't know if we want to do more…
**Tyler Yahn** 08:07 Yeah, I was kind of hoping he would be here to… talk about that.
Yeah, I would like to… get a release out. Kubecon is coming up, I think it's 2 weeks away, and so, I'd like to have something.
It's not, like, the end of the world, but it also would be really nice to have something, so… I… yeah, I kind of wanted to ask Mario, like, where we're at. I don't know, like, I'm also getting to the point where, like, it may just be, like, not necessarily, like…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:40 The downside of not having everything.
**Tyler Yahn** 08:42 That we want to… Not export… not unexported, means that, like, we may have to do this at a later stage.
Involving some sort of, like, deprecation process.
And so, it just becomes a little annoying. It's not, like, impossible. Like, it becomes impossible once we have, like, a stable release. So… I think that this isn't also meant to be, like, as much of a library. Obviously, it is somewhat of a library, because we have other, you know, projects importing this, and so there are things that, like, do have dependencies external to this, so we want to try to provide a sane API.
But I do, I do wonder… Yeah, I guess that's my question. Like, if Mario was looking to try to finish this up in, like, a day or two.
**Mario Macias** 09:31 Hello, sorry, I just joined.
**Tyler Yahn** 09:34 Oh.
**Mario Macias** 09:34 Yeah, I'm still working on this. I think there are some packages we can still… we can still, hide. Yeah, yeah, so… But I hope for this week, have most of this done. Last week, we were in off-site, we have had other issues this week, and I couldn't dedicate as much time as I would like, but it's still working, work in progress.
**Tyler Yahn** 10:02 Yeah, so I don't know how much you heard jumping in there, but, like, we have KubeCon coming up in, like, 2 weeks, and so the goal is, I think, try to get a stable release out, but I think also more of my goal is to try to get a stable release out and get Nimrod's Helm chart PR merged.
So, we need a little bit of runway on getting that Helm chart, PR merged.
for the KubeCon event, so ideally, I think, like, I'd love to get a release out, next week, sometime like that. Okay.
But it, like… it'd be really nice if we could resolve this, so I guess it's just more of a question of, like, do you think that that's possible? Like, we could get the packages.
**Mario Macias** 10:42 Yes, yes, I will, I will prioritize this.
**Tyler Yahn** 10:46 Okay.
Cool.
**Mario Macias** 10:48 the country.
**Tyler Yahn** 10:49 Okay. Yeah, that sounds great. I'm happy to, you know, obviously review PRs and that kind of thing, so… yeah, I think that sounds great.
I saw a lot of interest in, Imran's PR in the Helm chart as well, so I think that it's not just us looking to try to get this out, so, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 11:04 Yeah, it's a blocker for the, official, kind of, blog post announcing Obi.
**Tyler Yahn** 11:10 Okay, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 11:11 Yeah.
**Tyler Yahn** 11:16 So, yeah, definitely, I think… I think that timeline works. So, yeah, let's… let's, let's make it happen.
So, yeah, cool.
Well, cool, alright, that's a little bit jumping around. But then, yeah, so then, you know, I guess maybe coming back to Steven's thing.
adding a new package after, is not a problem. So that's… I don't think that's any blocker either. So, yeah.
Looks good.
Well, cool. I see, Mara, you're adding, Comment about the KubeCon OB slot time?
**Mario Macias** 11:54 Yeah, it's… it's in the… in the OpenTelemetry booth. Any slot… So, people can find us, talk about OBI, etc?
**Tyler Yahn** 12:06 Yeah, are you saying that you've signed up for this?
**Mario Macias** 12:10 I'm… I'm singing out for the maintainer's meeting.
But I will, I'll be also during QCon there.
**Tyler Yahn** 12:20 Oh, no, sorry, so, so, like, the slot, you have to, like, register it with the… I don't know, I think Antoine or something like that, and the GC is doing it.
So if you haven't yet, I can work on that, but I think it's a great idea, is what I'm saying. I just want to make sure that, like, it does happen. So yeah, if you've already, like, talked to them about it, then… Let's, let's, let's go for it, but otherwise, I can, I can talk to Antoine.
**Mario Macias** 12:47 Okay, if you point me to… to who or where to address, I can… I can do it myself, but as you prefer.
**Tyler Yahn** 12:54 Yeah, I think it is in the Hotel Maintainer's channel?
**Mario Macias** 13:00 Okay.
**Tyler Yahn** 13:01 Sorry, let me just take a look really quick.
Oh, here we go. Yes, I found there's a link here. I'm gonna put this in… the notes…
**Mario Macias** 13:23 Cool.
**Tyler Yahn** 13:23 Yeah, so there's this, yeah, there's this form here.
Yeah, so yeah, I think you should just be able to fill that out. Let's just open it really quick to make sure it hasn't, like, closed.
No. Okay, cool.
Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 13:36 Cool.
**Mario Macias** 13:37 Mmm.
Yeah, this is…
**Tyler Yahn** 13:39 That's great. Yeah, so if you just want to fill out this form, yeah, that sounds great. I think that's a great idea. Thanks for bringing it up, though. I… yeah.
**Mario Macias** 13:45 Okay, what do you think? Shall we run a session, or just asking that we would like to announce some slot where we will be, so people can come to talk?
**Tyler Yahn** 13:57 I think… I think… so, I'd probably say the SIG, I don't… I want to run a session at the observatory.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 14:10 Yeah. Oh, oh…
**Tyler Yahn** 14:13 Yeah, I just… I think… I think the talking thing is… I don't know how that gets entered into this form. But yes, I think… Yeah, I think what I've done in the past is, like, we've had, like, the GO SIG, just have their SIG meeting at the, conference. Usually it's, like, you know, a handful of people that show up, and we more just ask about, like.
any user experience, anybody who's interested, or something like that. So, you do get a lot of foot traffic that comes by, and so I think, like, should hopefully get people that are interested, or people that have used it.
Coming in, so I would rather do something, like, thinking about it more user-centric, and trying to just, like… you know, have something like that, instead of having, like, a presentation or something like that, I don't think… Yeah.
**Mario Macias** 14:56 Yeah, I agree. I agree.
**Tyler Yahn** 14:58 So…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 14:59 Reddit.
Mario, I was just thinking, like, if you wanna… we can just hang out at the booth and answer questions as people come by.
**Mario Macias** 15:07 Yeah, yeah, exactly.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 15:08 Yeah, exactly.
**Mario Macias** 15:09 That's…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 15:09 Just somebody… yeah.
**Mario Macias** 15:11 Yeah, that's why the… yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 15:14 Yeah.
**Mario Macias** 15:15 Yes, I was thinking to be at the booth, but maybe somewhere announcing or let people know that we will be there from the OB side, so people interested in OBI.
**Tyler Yahn** 15:26 Yeah, I think that that's… that's kind of the key, because, like, usually, you know, you kind of get a little bit of a clearing of a space, and people will just know to, like, come… come to a specific area to come talk to us. And I think it's good, because, like, you know, obviously the… the event is really busy, so they know, like, hey, I'm gonna be there at this time to talk to these people, so… yeah, I… yeah, I think that that's… That's a great idea. I don't know how long… like, we've done an hour in the past, and it's been… It goes by fast. So, yeah.
It's also, like, not a super.
**Nimrod Avni** 15:56 You mean, sorry, in the booth, you mean, like, the Gophana booth, or, like, a booth that we have set up specifically for OB or something?
**Mario Macias** 16:04 Yeah, the OpenTelemetry booth.
**Nimrod Avni** 16:07 In… okay, okay.
**Tyler Yahn** 16:09 Yeah, it's like, it's usually one of the, like, it's in the pavilion, obviously it's different every year, but it's, like, like, one of the larger event spaces is assigned to it, and then it's a whole, like, yeah, it's an hotel-specific thing. It's definitely not a vendor-specific thing, and it's just meant, like, to, yeah, if you haven't…
**Nimrod Avni** 16:28 We can definitely also come as well, same time.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 16:30 Yeah, yeah, you should. Like, if your guy's there, like, we should hang out on…
**Tyler Yahn** 16:34 Yeah, I… if this is… if you haven't seen it before, I would recommend, like, planning to spend as much time as you can at the hotel booth, because I think that's, like, where a lot of the conference really happens. Even outside of, like, these sessions, like, there's just so much organic conversation that people just come by and just try to talk about hotel there, so the more time you can spend there, the better. I think people love Seeing people and talking to people, that's where everyone's gonna be, yeah.
**Nimrod Avni** 16:58 Cool.
**Mario Macias** 16:58 Cool.
**Nimrod Avni** 16:59 Okay.
**Tyler Yahn** 17:01 But yeah, Mario, that sounds good. If you wanna… Yeah, just get this posted. I don't know, I think the schedule usually comes out, like, the day of the KubeCon, so I don't know when… But yeah, I think that's… that sounds good.
**Mario Macias** 17:15 Okay.
**Tyler Yahn** 17:17 It's also pretty flexible, if I remember correctly, so, I usually get stuck, on, like, the last day, almost in, like, the morning or afternoon, which always kind of stinks, but, yeah.
Okay, last thing on the agenda is I wanted to go through the open pull requests. There were a few, this morning. So, this toolchain, still something work in progress, definitely not as important as trying to get the other things.
Handle the, receiving large HTTPS payloads. So this is something, Nikola, I think we've looked at for, yeah, a little bit now. It looks like we have two reviews on it. I think this is… looks like ready to merge.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 17:58 I have some comments from Matt, so I'm gonna address them, and I think it should be fine.
Okay.
Yeah, questions and comments, so I… I need to go through them, it's probably a good… Good feedback, so…
**Tyler Yahn** 18:12 Cool, okay, yeah, then, yeah, we'll look at some iterations, but yeah, this looks great. So this is, yeah, I mean, I'm pretty excited about this, so… Thanks for putting this together, it was a lot of work, so yeah, I appreciate it.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 18:23 Yeah, a lot of edge cases, some of them are exposed by the work that I did, I kind of… Changed things a little bit, and then… I… I found a lot of the root causes why we had those intermittent test failures on some of these tests, so, So hopefully this stabilizes also the CI quite a bit, but…
**Tyler Yahn** 18:44 Yeah, one can hope, right?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 18:45 Yeah, we're careful, yeah.
**Tyler Yahn** 18:49 Okay, cool. This next one is a dependency update. I wanted to actually ask the Grafana folks about this one, because, this just breaks all of the, testing, and I can't quite figure out why. Like, I mean, I can figure out that it's not… finding, attributes that it expects, but I can't quite figure out why that's the case, I guess.
I don't know if… this is really obvious…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 19:14 Yeah, I took a brief look, look at this, I have no idea, looks like it… Like, the queries did not produce results.
Maybe some sort of escaping issue, no idea, but we can take a look. It shouldn't have broken like this.
**Tyler Yahn** 19:30 Okay.
Alright, yeah, I… yeah.
I was pretty lost, sounded like you were just as lost as I am, so, okay, I… yeah, we'll take a look then.
Okay, and then the last thing that we have open is a max transaction time. I haven't taken a look at this one yet.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 19:48 Well, it obviously doesn't work what I did, but, I can explain what this does. It's… I found cases where these massive transactions happen, and one is in the hotel demo. There's a load generator, just keeps on generating load. We instrument it, and then it looks like infinite amount of client requests under the same transaction. It's just the thread just keeps on producing more and more clients, and… And it's just never gonna stop, so just grace this insanely large traces.
So, What I thought about doing is… we need to break it up somehow, and kind of mark it as invalid, so it stops doing that. So these are at least chunked in multiple, or they appear as single traces that are just the client. Starts with the client rather than It gets all wrapped in one single server.
So for that.
reason I added, like, a maximum, sort of, transaction expected time, so 5 minutes. Anything longer than 5 minutes, we consider that's… those relationships are not valid.
To cause this to… to stop. I've seen other cases in the field that people have reported, Kafka is one thing, like, you're gonna launch a transaction that kicks a background thing, and it just keeps on sending Kafka events.
Non-stop, and that appears like one big badge job that… May last for days.
It generates some traffic. People kick off background tasks from HTTP requests, so they'll kick off an HTTP request that starts a background task, and we take that context of original HTTP request, and then everything that happens in the background tasks.
is nested as a… Child, so… Yeah, so this proposed us to do that.
To kind of, like, put a cap on what's reasonable.
And, break up the transaction.
**Tyler Yahn** 21:58 Yeah, I mean, that seems reasonable to me. It's… it's configurable too, right?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 22:02 Yeah, yeah, I've set it to 5 minutes, I thought that even, like.
something like OLAP request, they should finish in 5 minutes, I don't know.
But.
**Tyler Yahn** 22:15 Yeah, I mean, starting somewhere is fine, right? Like, you gotta choose something.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 22:18 Yeah.
But I think my math around… I added a test, but I think my math around the nanoseconds and the BPF reported time is off, so I think I'm probably breaking everything. I need to look into why the test failed, but…
**Tyler Yahn** 22:33 Okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 22:33 No.
**Tyler Yahn** 22:35 Yeah, that makes sense.
Okay, cool. Well, yeah, we'll keep an eye on it, wait for an update on the testing. But yeah, thanks for putting this in, I think that makes sense.
Okay, yeah, I think that was it. Yeah, so that's the end of the PRs. We talked about the milestone already, so that's the end of the agenda. I'm gonna pause here. Any other topics people wanted to discuss that haven't been added to the agenda yet?
**Mario Macias** 23:04 Just inform you that this morning, I have recorded a podcast channel from… a podcast episode from this Open Observability podcast. I don't know if you… if you know from Dothan, Horovitz, I think it's… Yeah, we talked a bit about the donation.
We have mentioned all the companies involved in this project, and so on. So, yeah, probably by the end of the month, it will be public.
**Tyler Yahn** 23:40 Yeah, that's funny you said that. I just saw that on, like, LinkedIn. So, yeah, I'm excited to hear it. If you do, like, I think it was, like, the 27th or something it comes out, but yeah, when it does come up, please make sure you post it in the Slack channel, the eBPF Slack channel, so, yeah.
**Mario Macias** 23:57 Okay.
**Tyler Yahn** 23:58 Yeah, because I… one, I want to listen to it, so that's, you know, a little selfish there, but, like, two, I think that just popularizing it and making sure we, like, you know, talk about the project, I think that's a great way to do that. So, yeah, definitely share it as much as you can, please, yeah.
**Mario Macias** 24:13 Cool.
Yeah.
**Tyler Yahn** 24:15 Yeah, awesome. I'm excited. How long was it? Was it, like, a half hour?
**Mario Macias** 24:19 One hour.
**Tyler Yahn** 24:20 One hour, okay, cool, yeah.
**Mario Macias** 24:22 Awesome.
**Tyler Yahn** 24:24 Yeah, I think this project has a lot of, like, value, and so, the marketing side of things is always something I fail at, so I think this is great to see these sort of events and these sort of, like, talks at KubeCon, these sort of, like, podcasts. So, yeah, I think blog posts as well are another thing, so I think we can try to keep the project going, yeah.
Awesome. Any other, sweet publicity events from anybody else?
No.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 25:02 Well, we have two talks at KubeCon. I think Maria's talking as well.
**Tyler Yahn** 25:07 Oh, nice. Yeah. Yeah, that's also… are you main session, Mario, or are you the observability days?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 25:14 In the main session.
**Tyler Yahn** 25:16 Alright, yeah.
I imagine that they've scheduled your talk exactly at the same time as my talk, or… My talk, yeah, so I can't see it, but… I'm just joking, I don't know, but, like, yeah.
**Mario Macias** 25:27 Take a look.
**Tyler Yahn** 25:28 Yeah.
But yeah, that sounds great.
Yeah, I'm actually really excited, there should be a lot of really good talks. I've heard some other folks talking.
Talking there, so yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 25:39 Nice.
It's tough.
**Tyler Yahn** 25:42 Yeah, okay, well, cool, we can probably end it early here. Thank you, everyone, for joining, a lot of work, so yeah, it's all appreciated. I will see you all in a week's time, or, asynchronously. Until then.
**Giuseppe Ognibene | Coralogix** 25:55 My wife.
