SIG: SIG Injector
Date: 2026-03-02
Duration: 21 minutes
Zoom Recording URL: https://zoom.us/rec/share/FLRWrRVD40eG5YQBJOLMCO-p4GSmKnrxuCPg1Cr5wsfV-3vTFoqqlgVDazXXpwY_.HQiEIvoxdil6a6Zo
============================================================

## Zoom Recording Transcript

**Bastian Krol** 01:27 Hey there.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 01:29 Hey, Rasun, how's it going?
**Bastian Krol** 01:32 I know you.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 01:33 I'm good.
Just you and me,
**Bastian Krol** 01:41 For now?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 01:42 Yeah, I see.
**Bastian Krol** 01:43 Somebody… I mean, I don't think we had…
topics, to be honest, or at least I… Don't have any…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 01:53 Yeah, there doesn't seem to be anything on the agenda.
**Bastian Krol** 02:05 Maybe that's… Give it 5 minutes, and if nobody shows up, we… Can probably… Cancel it. Yes.
Hey, Kyle. Hey, Antoine.
**Kyle Wang** 03:46 go.
**Antoine Toulme** 03:47 Hey.
**Bastian Krol** 03:57 So it's all already 4 minutes past the hour, I guess. We can start…
We don't have anything on the agenda, though, so…
**Antoine Toulme** 04:09 Okay.
**Bastian Krol** 04:12 It could be a short one. Maybe someone has topics spontaneously, or wants to talk about something.
**Antoine Toulme** 04:23 I do not.
**Bastian Krol** 04:31 Can I give a very quick update on the release process stuff? So… just to inform you, I talked about that last week, that we need a specific or a custom
GitHub app, and just this weekend, this was… Ted up by the,
Auto Community Repository, folks, Trask.
Not sure what's his real name? I guess it's just his guesstar Pendle, I don't know.
And…
I just merged that into our own repository, so I guess I'm trying a release later today, or maybe two tomorrow, and theoretically, it should just go through then, but we'll see.
**Antoine Toulme** 05:19 Great. That's awesome.
**Bastian Krol** 05:22 Yeah.
Not really.
**Michele Mancioppi** 05:24 Talk about, Trask.
**Bastian Krol** 05:27 Trusk, yes.
**Michele Mancioppi** 05:29 It's his name.
**Bastian Krol** 05:30 This is, it's actually its name. Interesting. Okay.
**Michele Mancioppi** 05:33 As Karnaka.
If I don't remember correctly.
**Bastian Krol** 05:36 Yeah, okay.
And that, that's the guy, yeah.
**Antoine Toulme** 05:41 Okay, cool.
**Bastian Krol** 05:42 Yeah.
**Antoine Toulme** 05:43 Perfect, thank you so much for working on this.
**Bastian Krol** 05:46 Yeah, sure.
Welcome.
Anything else that's on your minds?
Michael, you were a bit late, we just recognized that we don't have anything on the agenda, so no one has anything…
No topics.
**Michele Mancioppi** 06:04 No, you're tempting me, right?
**Bastian Krol** 06:07 Yeah, yeah. Something just becomes…
It's famous last word, asking Michele if he wants to talk just about anything at all.
**Michele Mancioppi** 06:15 If I have something urgent on my mind, right?
**Bastian Krol** 06:18 Yeah.
**Michele Mancioppi** 06:21 Oh, in reality, I mean, it's, we are a bit stalling on,
a few things, but I think it's mostly because there is this
Big question hanging in the air about, packaging.
So I would love for somebody to…
To look at the PR.
I did for the packages and tried out properly.
I'm wondering if we should just…
do something ourselves inside the SIG until we get the packaging SIG out, but…
And I would love to be able to help somebody from OBI.
to start talking about how OBI should fit those packages.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:10 There we go.
**Antoine Toulme** 07:10 Okay.
Yeah, where are you thinking, Claire?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:17 Yeah, I can be the person.
Is this discussed in the packaging SIG?
**Michele Mancioppi** 07:23 The packaging sick doesn't exist yet.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:25 Okay.
**Michele Mancioppi** 07:26 I'm waiting, so at the moment, TPR on the community.
Is, hanging on internal, steering committee things.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:35 Okay.
**Michele Mancioppi** 07:37 mostly, I think that the big thing that's missing is…
For them to decide what type of engagement from the technical committee, if it's leading, if it's a company, or whatever it is, and who is the sacrifice upon them for that.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:54 Okay.
I can be that person, I don't know how… how do you… how do you want me to help? Talk on the issue?
**Michele Mancioppi** 08:00 So there is, there is an, in the community PR,
There is, a specification which
I'll close the PR if I haven't done it yet. I created a project… oh, no, there is a project file.
Okay. Which is a factory, the funding charter for the packaging sake.
And there, there's language about, hey, how should
OBI and the injector play nice together, because I was talking with, I want to say Marios, or Mario?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:34 Mario, yeah.
**Michele Mancioppi** 08:35 Mario, in Brussels.
Okay. And, I mean, there are… the support metrics of the injector and OBI are different.
And,
some of the things that OBI does, the injector does as well, like, for example, putting the auto-Java agent.
inside, Java applications, and I think we need a,
a valid story of how they work together, or OBI is the best solution in system packages where allegedly you have access to a kernel, so we need to figure that one out.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:12 Okay.
Yeah, alright.
I have some ideas.
**Michele Mancioppi** 09:16 The whole discussion about declarative configurations.
Because, in my opinion, the clarity configurations is the right way to go for system packages, but OBI doesn't implement it, as far as I know.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:29 We do now. I mean, it's in progress, there's a PR open
Without Configuration 2.0, we're trying to agree on…
**Michele Mancioppi** 09:38 Toilet.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:38 how it's gonna be, Tyler's driving it, yeah.
**Michele Mancioppi** 09:41 That's terrible.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:43 So it's gonna happen. The new format is so much better than what we have. What Tyler came up with is very good. I really like it, so…
We're trying to… Figure out the format, and then we're gonna go and implement it.
**Michele Mancioppi** 09:59 I was very surprised.
To… to see. From the YouTube video I posted in the…
In the, packaging, in the, in the SIG, in the injector sig.
That, Adam from DataTrace actually used the packages for one use case that I specifically marked as not core, that is to build container images.
And I don't know if it is…
Unfortunate, or it is a signal?
Final.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 10:33 Which YouTube video is this? Have you posted something?
On the injector.
Okay.
Alright, I saw this.
**Bastian Krol** 10:53 Well, I mean, technically, there's nothing wrong with that, right? I mean…
But…
**Michele Mancioppi** 10:59 There's nothing wrong.
I, I just marked it as non-core, because…
Why would you put it in a container image when you can have the OpenTherent operator do it for you?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 11:21 Yeah.
**Bastian Krol** 11:21 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 11:22 to do this with the operator, right?
**Bastian Krol** 11:25 I mean, container images are not necessarily on Kubernetes, right?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 11:29 Yeah.
**Bastian Krol** 11:31 So that's still a different level.
**Michele Mancioppi** 11:35 I think…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 11:37 Yeah, Mario and I are hacking on a…
Or something to do this with the injector as well.
This is a hackathon week here at Grafana, so we're trying to do… at the OCI image.
To have it use an injector.
some people that run, I don't know, Doc Compose and bring up their stack, there's those people, I guess, as well.
And we made sure what it would take to run both OB and the injector on a host.
Out of the box, see what kind of got gotchas.
skip all the system services and things like that. It's more of an OB issue than it is with the injector, but…
We want to try to see what it takes to create a default config that's reasonable.
I tried the injector together with Obi on the Istio demo, it did quite well. I really liked the outcome, because…
We have extended Istio demo as Go applications and all this stuff, and…
The hotel injector instrumented everything that was… Java, Node.js…
net, and then, oh, we picked up the Go applications and all nicely worked together, so…
**Bastian Krol** 12:55 Nice.
**Michele Mancioppi** 12:55 That's quite cool.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 12:57 It's very cool, yeah.
I'll try to clean up the demo. We just did it on Friday, kind of, like, rushing to see if this will work.
I really like that story, so…
**Michele Mancioppi** 13:07 That's pretty cool. And OBI has, OBI can, detect, hey, the person already has SDKs inside, right?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 13:14 Yeah, yeah, yeah. And that was the point, I wanted to see if it worked for real, right, on a demo that I haven't seen before.
And… He detected that these were instruments and left them alone, and…
**Michele Mancioppi** 13:28 That's very cool.
**Antoine Toulme** 13:33 Yeah, I need to finish the blog post, right? I mean, if you want to take over the blog post to explain OB versus Injector, feel free. If not, I'll…
I need to do it, I just, just need to do it.
So, that might be a good way.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 13:49 Oh, dear?
Yep, can we put that on my list?
**Antoine Toulme** 13:53 Pretty much, I would just summarize whatever you just said into a blog post form.
And ask you for review.
She's been worse.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 14:07 Nice.
**Michele Mancioppi** 14:15 I mean, effectively, we need,
When I look at the support metrics, For the declarative configuration format.
And Obi is coming up with it.
Java has it.
Yes. No guess, has it.
That, the injector supports were missing .NET and Python.
So, Antoine, what are the Splankers doing about it?
**Antoine Toulme** 14:45 I'm not sure. It's a good question. The other thing is, the decorative config for Java, yeah, you hear a lot of rumblings about Java having it.
And then you start to scratch. I'm closer to the Java guys, right? And,
They tell me, not everything is well supported. I'm like,
Please, elaborate. What do you mean? So, I'm not… I'm not hearing a whole lot of good things about, like, how well they are at this point. And I think you…
maybe unintendently, what we're going to do is we're going to find all the cockroaches. We're going to…
Without even trying, put them to a benchmark.
Does that make sense?
**Michele Mancioppi** 15:33 I am less worried about partial implementations, or a bit buggy ones, than I am about entirely missing implementations, like .NET and Python.
**Antoine Toulme** 15:42 Okay, I don't know, like, both are a problem, but you're right, that missing the whole thing seems like a bigger issue.
**Michele Mancioppi** 15:52 Because in reality, I mean, the, the…
Like, when we take it from the point of view of the system packages.
**Antoine Toulme** 15:59 Yep.
**Michele Mancioppi** 16:01 when we think about a virtual host, then you are going to want a collector.
Nearby.
Yep. So… Multiple exporters, Don't really care.
**Antoine Toulme** 16:15 But at least for the declarative use cases.
**Michele Mancioppi** 16:18 If I had to read the resource attributes.
the detectors.
**Antoine Toulme** 16:23 Yep.
**Michele Mancioppi** 16:23 Serve his name.
And, the, instrumentation's on and off.
I don't think that in a situation with, on virtual host, you need much more than that. Not from the point of view of virtual applications.
**Antoine Toulme** 16:39 But that's… that's here, that's your functional test suite, in a sense, right?
So we want to aim for this level of functionality from declarative config.
So we can base ourself of it, is that right?
**Michele Mancioppi** 16:54 Yep.
**Antoine Toulme** 16:55 Okay.
Yeah, no, I don't know what's happening with Python. It's always been a bit of a… less of a…
We don't have a maintainer on the Python SDK that I know of.
So… We can ask the Pyth and see.
**Michele Mancioppi** 17:18 Maybe, Nicola, you have more Grafana side, more info?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 17:22 No.
No, we don't have anybody working on Python.
**Michele Mancioppi** 17:28 Yes, we're…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 17:30 Hmm?
**Antoine Toulme** 17:30 We're gonna have to invest a bit more.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 17:33 I know.
**Michele Mancioppi** 17:35 No, I, I intend to staff this year somebody to work on the Python SDK almost full-time on their steel side.
Because the dead thing needs help.
**Antoine Toulme** 17:45 Yeah, it does. I think you identified that.
Couple times.
**Michele Mancioppi** 17:49 Actually, if you actually know of good people that are outside the observability world, but they like to contribute to a Python SDK.
**Antoine Toulme** 17:57 Ugh.
**Michele Mancioppi** 17:58 I'm all yours.
Because instead of hiring somebody from a competitor, I would rather hire somebody who's not doing it full-time to do it full-time.
**Antoine Toulme** 18:07 Yeah, it's a small… it's a small cottage industry at this point, right? We really need to.
**Michele Mancioppi** 18:13 to go and, hire some people. Get some fresh blood.
**Antoine Toulme** 18:16 Fresh blood, yeah.
**Kyle Wang** 18:19 No, sorry.
**Antoine Toulme** 18:22 Yeah, go ahead.
**Kyle Wang** 18:23 Oh yeah, I just sent a thread. Assume it's kind of related to declare config on the Python.
**Michele Mancioppi** 18:28 Pretty much.
**Antoine Toulme** 18:29 So…
**Kyle Wang** 18:30 Yes. But it's still a work in progress, from my understanding.
**Antoine Toulme** 18:41 Thanks, Kyle.
**Kyle Wang** 18:42 And from our side, I don't think we currently have enough people to start working on this. It seems like there's some community efforts on this.
**Michele Mancioppi** 19:02 It'll be nice.
I mean, the moment that we can have, we can rely on the collective SDKs on later versions.
I think we can make a kick-ass experience.
On, on Linux, across the board.
**Antoine Toulme** 19:50 Agreed.
I… sorry, that's all I can do at this time.
**Michele Mancioppi** 19:54 Yep.
By the way, since I have you here, Antoine.
What happened with the, Auto Observatory at KubeCon?
**Antoine Toulme** 20:03 We're not doing it this time.
**Michele Mancioppi** 20:06 Why?
**Antoine Toulme** 20:07 So we've done it a couple times now, and
it was well received, but we felt that, first, we wanted to make sure that we were using the space from the open source, because all open source projects of the CNCF actually have tables that are supposed to be available to them.
I'm learning that the DC needed to reserve them, and they did not, so there's maybe some issue there, but that's a different discussion. So the other is we…
We want to make sure that, we don't just repeat the same pattern over and over. We want to kind of give also, like, a way for the community to meet, that's just there. And, it's interesting, because we… we were told, like, last time, it was like, the observatory's kind of a…
not that fun, we could really do all the things, and so we decided to just stop this time and see what happens. And interestingly, people are coming out of the…
And telling us, no, actually, you like this? What are you doing?
But, okay.
So… That's… that's where it's at.
**Michele Mancioppi** 21:26 Me too.
**Antoine Toulme** 21:32 Okay, I managed to run, so folks, I'm sorry, but great catching up. I'll see you next week.
**Bastian Krol** 21:39 around… alive.
