SIG: Community Demo App SIG
Date: 2026-09-23
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Donal O'Sullivan** 00:30 Hey, Juliano.
**Juliano Costa | Datadog** 00:36 Hello, hello!
Good afternoon.
**Donal O'Sullivan** 00:40 How are ya? Are you, are you, are you, are you in, in, Brazil still? No, you're home, are you?
**Juliano Costa | Datadog** 00:46 Yeah. Yeah, I'm still here, and it's like…
**Donal O'Sullivan** 00:49 Cool.
**Juliano Costa | Datadog** 00:50 To our lunch time here now.
**Donal O'Sullivan** 00:53 Nice. How's the weather? Is it melting hot, or is it already?
**Juliano Costa | Datadog** 00:56 It was raining a lot, but yeah, temperature-wise, it's okay. Like…
**Donal O'Sullivan** 01:05 Yeah.
**Juliano Costa | Datadog** 01:07 Colder than usual, for my hometown, but yeah.
Wow.
**Donal O'Sullivan** 01:13 Okay.
Are you originally Brazilian, or are you… you're Portuguese? You're Brazilian?
**Juliano Costa | Datadog** 01:19 No, Brazil. Cool, cool.
**Donal O'Sullivan** 01:21 Oh, cool.
**Juliano Costa | Datadog** 01:22 My hometown is called Araraquara.
**Donal O'Sullivan** 01:26 Okay, cool, cool.
**Juliano Costa | Datadog** 01:27 That's, countryside of, Sao Paulo.
**Donal O'Sullivan** 01:32 Nice.
**Juliano Costa | Datadog** 01:33 Yeah.
**Donal O'Sullivan** 01:33 So it was a good… it was a good, maybe a trip to… a nice expenses-paid trip to get back to… back… back home for a bit, maybe, was it?
**Juliano Costa | Datadog** 01:41 Yeah, I got a trip to Sao Paulo, so, like, everything that I… everything I did in those two weeks between… the… the event, last week, and the KCD that is happening this weekend. Everything I did, I did on my own, but, like, the… the… the… biggest expense is the… is the plane, so, like…
**Donal O'Sullivan** 02:07 Yeah.
Yeah, yeah, exactly, yeah, yeah, yeah, such a far… so far away, like… Yup.
**Juliano Costa | Datadog** 02:15 Yeah.
And of course, I visit my tattoo artist, so the… The arm is, like, getting colorful.
**Donal O'Sullivan** 02:30 Nice, nice, very good, very good.
Cool.
**Juliano Costa | Datadog** 02:34 How are things on the demo side?
Yeah, speak.
**Donal O'Sullivan** 02:44 I joined, but no one joined, so I just left. I'm fairly busy at the moment, I have a lot of… I have a lot of work to do with the Elasticsearch Explorer, Just for Elastic at the minute, so I… I haven't had a huge amount of time to look at the demo, but I'm trying to get to PRs that I… that I'm… that look relevant to me, like… The only reason I messaged you about… I don't want to be, like, going on about negative things, but I… that person getting blocked… I just noticed sometimes you jump into a PR, and there's, like, huge walls of text, and it can be, like, a bit of a, like, I don't have the time for this part, do you know what I mean? Because it's usually, for me, it's like, yeah, this person just AI slapped it, and they're copying and pasting the AI texts into the PR, and… Yeah, maybe I need to be more proactive, like, could you… Do… do we have that button on the PRs yet? Maybe I could add that, or something like that, just like, please write… please don't use AI for PR description, or whatever the hotel way is.
**Juliano Costa | Datadog** 03:50 I, I think we do… I think the, the agents.md tells… explicitly… explicitly that? If not, Definitely, and?
**Donal O'Sullivan** 04:04 Hmm.
**Juliano Costa | Datadog** 04:05 I don't know why the… all… all our builds are failing.
**Donal O'Sullivan** 04:12 Oh, shoot, are they?
**Juliano Costa | Datadog** 04:13 Yeah.
And the butts.
**Donal O'Sullivan** 04:16 Is it?
**Juliano Costa | Datadog** 04:17 Yeah.
Like, even the… even the… like, GitHub code, GitHub Actions, images.
They're failing to update, because…
**Donal O'Sullivan** 04:41 about it.
**Juliano Costa | Datadog** 04:42 The CI is failing because the CI is failing on the telemetry.
Telemetry test, build.
**Donal O'Sullivan** 04:49 Yeah, it looks like it timed… so telemetry tests are timing out.
So, just at the end, it says the… the… Run telemetry test is timed out after 15 minutes.
**Juliano Costa | Datadog** 05:02 You know what?
Maybe the… haha… Yeah, maybe that's it. Maybe we need to increase the time, because we replaced, we reverted the… Theologian.
**Donal O'Sullivan** 05:20 Oh…
**Juliano Costa | Datadog** 05:21 And now we are using, locust.
**Donal O'Sullivan** 05:25 Yeah, they're… they're slower than… what was the other one? K9 or something, was it, or what was it called again?
**Shenoy Pratik** 05:32 K…
**Juliano Costa | Datadog** 05:34 PC.
**Donal O'Sullivan** 05:34 K6, yeah, yeah, sure, that was gold, and this is…
**Shenoy Pratik** 05:37 Are we talking about the timeout issue on telemetry tests?
**Donal O'Sullivan** 05:42 Yeah, all the Dependabot PRs are failed, the CI fails, and run… Yeah, I was…
**Shenoy Pratik** 05:47 thinking what was causing it and trying to fix it, I presume it was related to some open search issue.
for log ingestion that was causing this, and I have a draft PR.
Let me just move it out.
To read you for review.
That's what I saw in my local test, I'm not sure if this will fix it.
I need to double down on it and, like, look at the actual issues, in the logs locally. But what I'm seeing is, something changed the card service… Log HTTP attribute.
And that's conflicting with the open search mappings. It's not conforming to OTEL semantic conventions, which other services are doing correctly. And because of the conflict, the logs that are coming from card services are not going in, and that's causing the telemetest to fail.
That's the initial hypothesis.
I need to dig down further, but that's what this PR does.
**Donal O'Sullivan** 06:54 Sorry, Shenoy, but what caused that? Was it because of the revert to locust, or was it something, some other change that caused that?
**Shenoy Pratik** 07:02 That's what I'm not sure about. It's not revert to Locus, for sure, because that was done way earlier.
I'm looking at, Juliano's PR, and it has some version bumps to OpenSearch and some other places as well.
**Donal O'Sullivan** 07:20 Okay, yeah.
**Shenoy Pratik** 07:21 And this…
**Donal O'Sullivan** 07:21 Maybe there's something there.
**Shenoy Pratik** 07:22 one of the version bumps might have caused something. It may be the collector as well, because I know OpenTelemetry Exporter has some updates.
So… I'm trying to figure out, like, which is the exact root cause, but this is one of the suspects that I caught on the way.
Yeah.
I ran the test locally on the current draft, it looks good, but if you can run it on…
**Juliano Costa | Datadog** 07:50 I… I can… I can, I can approve the PR, but can you remove all the comments on the compose.yaml?
**Shenoy Pratik** 08:01 Yes, yes, yes, yes. I think I… Or did I… came back again.
**Juliano Costa | Datadog** 08:08 Good.
the… AI is… it's getting out of hand, like…
**Shenoy Pratik** 08:17 I explicitly asked it to remove, like… these stuff, and then add it in back there, okay.
Let me do it right now.
Yeah, I'll update the PR, though. It's fine to, not approve it.
If either of you can just pull this down locally and then run it, that would be helpful. Otherwise, I'll just fix it right now, and then we can approve it after the meeting.
**Juliano Costa | Datadog** 08:42 Ugh. Bit fool.
Will… will you… will you do it… I can do it via GitHub as well.
**Shenoy Pratik** 08:54 You can do it by any time.
**Donal O'Sullivan** 08:56 If I just approve the PR, though, it should run the check, right? It will run the check.
**Juliano Costa | Datadog** 09:00 Yes, we'll listen.
if you approve the PR and he updates the PR.
**Donal O'Sullivan** 09:05 Yeah.
**Juliano Costa | Datadog** 09:05 Yes, we'll be canceled.
**Donal O'Sullivan** 09:07 Yeah, true, yeah.
**Juliano Costa | Datadog** 09:08 We don't need to re…
**Donal O'Sullivan** 09:09 Yeah, yeah.
**Juliano Costa | Datadog** 09:09 Yeah. There are PRs that I, like, I approve, then they're running, and then the owner rebates.
**Donal O'Sullivan** 09:17 Pushes a change.
**Juliano Costa | Datadog** 09:18 And then…
**Donal O'Sullivan** 09:18 Yeah, yeah. It cancels. You're like, no! Why'd you do it?
**Juliano Costa | Datadog** 09:22 Now I need to re-approve.
**Shenoy Pratik** 09:26 Yeah.
Let me do it via GitHub directly.
**Juliano Costa | Datadog** 09:42 What else? What else? We have the… spring for, PR that I would like to discuss here.
Spring Boot.
Oh.
**Shenoy Pratik** 09:59 Yeah, I went through the PR, I think even Donald went through the PR. I'm just thinking, does… I'm not aware of the Spring Boot side and OpenTelemetry side of things there, on the other end of Java, where, do they recommend using their own framework? There is some framework that they have, right? Meet or something.
**Juliano Costa | Datadog** 10:23 Is it…
**Donal O'Sullivan** 10:24 Spring Boot is a framework for Java for web services, right?
**Shenoy Pratik** 10:28 They have… they have another OpenTelemetry library.
**Donal O'Sullivan** 10:33 Oh, okay.
**Shenoy Pratik** 10:34 And they do not confirm to everything OpenTelemetry.
It's for Micrometer area, yeah, that's what I was doing.
**Donal O'Sullivan** 10:41 Oh, okay, okay.
**Juliano Costa | Datadog** 10:43 Yeah, me too.
**Donal O'Sullivan** 10:44 The only concern I had with this, Pierre, was, Java can be a bit annoying with Docker, like, it can have quite a large memory footprint, and it can, like, hog, like, a lot of resources. I think you have to set some flag to tell it to stop, but by default, it will, like… so, like, if you run it in, say, a Kubernetes cluster, for example, if we run it locally in kind.
it will… and I have restrictions in kind of how much resource to use. The Java virtual machine will just use all the memory available on my system.
So, like, yeah, it's really weird, like, I don't know what the hell it does, like, it's… there's something… I don't know, it's something… I need to look into it a bit deeper, but it's something I found where if there's something weird going on with it, it will use, like, if I have 32GB RAM on my machine, it will allocate that much RAM, like, memory for the Java service to run in, even if you say, like, the kind service only has, like, whatever.
And, yeah, straight off the bat, I was like, oh, so we're going to Java. I don't know if this is going to be… Like, that's my only real concern, and I think I tried to run… I ran it locally.
And I… I don't… I use… I've got Arch Linux, I don't have a Mac, so it just didn't run, it just… it failed to build the actual… and I… yeah, that was my only issue with this work, so…
**Juliano Costa | Datadog** 12:03 Yeah, I think the failed to build, we need to address. It shouldn't be a problem.
Yeah. The… regarding the memory limit, for Java and Go, they have a different perimeter that we need to set.
I think we are… we are setting in Kafka and Ad service already.
If I'm not mistaken.
**Donal O'Sullivan** 12:29 Yeah, I think so, yeah, I think you're right.
**Juliano Costa | Datadog** 12:30 And,
**Donal O'Sullivan** 12:31 XMF, or XMMX, maybe, or something like that. I think it's set in the PR anyway, but…
**Juliano Costa | Datadog** 12:38 Oh, okay.
**Donal O'Sullivan** 12:38 Yeah.
Yeah.
**Juliano Costa | Datadog** 12:40 Yeah, because PRA is sneaky, yeah. It will just, like, yeah. Oh, yeah, the container limit is 100 in, maybe a bit… yeah, I don't care. I'll just use your whole… your whole system.
**Donal O'Sullivan** 12:52 Yeah. What's available in the system? I'll just use that. They're like, what the fuck?
**Juliano Costa | Datadog** 12:58 Why are container… why are container limits there? If you ignore, like, what's the.
**Donal O'Sullivan** 13:04 I know, yeah, yeah, it's… yeah, yeah, yeah. I think, like, Docker will… we'll abide by it, but if sometimes… I think in Kubernetes, it's like a soft limit, and if it needs more, it'll just go, go, it'll just say, oh yeah, there's more available, I'll use that, and then… Bang.
**Juliano Costa | Datadog** 13:23 Neo.
I have, another thing that we… So, I feel that Spring Boot is one of the biggest frameworks for Java.
**Donal O'Sullivan** 13:37 Hmm.
**Juliano Costa | Datadog** 13:38 the most used one, so I think having that on the demo is something useful. And, I also feel that having a micrometer instrumented service It's also interesting because… Micrometer is also a thing that existed Pre-existed hotel.
And a lot of Java developers use Micrometer?
So, I think it's kind of a nice-to-have.
I don't know if we should, actually do it, but, Because, like, it's the OpenTelemetry demo, not the micrometer demo, or whatever.
**Donal O'Sullivan** 14:22 Yo.
**Juliano Costa | Datadog** 14:22 But, like, I think it goes… On the same… On the same direction as we have with the chatbot, where we have, like, the… OpenLL Emmetry instead of hotel, because OpenLL Emmetry is more used than something, like, so… Hmm…
**Shenoy Pratik** 14:45 I have an, I have a point there. Like, for agents, Hotel SDK is not there yet.
I can make that statement. But with Spring Boot, I was also reading down on the hotel blogs that we have, and the documentation. That we have a starter pack which tells us, like, you have auto-instrumentation that comes out of the box.
And that there's more to the hotel conventions than… But on the other side, Spring Boot blogs have, like, explicitly mentioned that their version of OpenTelemetry is via Micrometer API. I got confused there.
Do you want to present what Spring Good tells is their OpenTelemetry GoTo APIs, or do you want to stick to hotel SDKs and… Auto-instrumentation part that we tell in our documentation, the open telemetry world.
It's kind of conflicting there.
I just went into this rabbit hole because, some of the micrometer APIs, sorry, attributes are not adhering to hotel convention. Like, that was the starting point, then I went into this rabbit hole.
But anyways, this is something that I considered. I don't mind, to be honest, either way, but if we can pull it out of micrometer into what we mentioned in documentation as a good starter pack for Spring Boot, we… can do better there, so that people try using the starter pack, see what is missing, and then we update the actual hotel side of things as well.
**Juliano Costa | Datadog** 16:23 I don't know.
But I think for OTEL, we have… for Old Tunnel, for Java, we have, Maybe…
**Donal O'Sullivan** 16:38 And can… can… go ahead, Julian, sorry. Go ahead.
**Juliano Costa | Datadog** 16:41 No, no, go ahead, go ahead.
**Donal O'Sullivan** 16:43 Could we not, like, instrument it with both, have, like, micrometer instrumentation, and then maybe have hotel instrumentation?
Just to show, it's kind of quirky, maybe, but…
**Shenoy Pratik** 16:56 Yeah, maybe we can do that, then that's the right path ahead.
**Juliano Costa | Datadog** 17:02 I don't.
**Donal O'Sullivan** 17:03 Just a show for spring booth, you know.
**Shenoy Pratik** 17:05 Yeah.
I'm just worried about, like, disconnected telemetry or deep telemetry.
**Donal O'Sullivan** 17:13 Duplicate, yeah, yeah.
**Shenoy Pratik** 17:29 Yeah, I'm not updated with, Spring Boot here, so probably if you guys have more information, we can present it. We can ask the author itself, present our points there, and let… The ones are the views that they have.
**Juliano Costa | Datadog** 17:46 Yeah, that's… that's actually a good point. We… we could, maybe raise on the… Hotel Java channel.
hotel Java instrumentation, and maybe someone from the Java SIG can jump in and give us a help on reviewing.
I… I'll do that.
Let me see…
**Shenoy Pratik** 18:21 I see one Java instrumentation that is archived here.
Is it… Oh, there is hotel Java.
**Juliano Costa | Datadog** 18:31 Yeah, we have… I think we have Autel Java and OTEL Java Instrumentation, if I'm not mistaken. No, I think the Java instrumentation was renamed.
Give me a second.
**Shenoy Pratik** 18:42 It's just total hyphen Java.
**Donal O'Sullivan** 18:46 Yeah.
**Shenoy Pratik** 18:47 Hmm.
**Donal O'Sullivan** 18:52 Yeah, there's hotel driver, yeah.
**Juliano Costa | Datadog** 18:55 Yeah.
Okay.
We have the Java maintainers, and we have the Java instrumentation maintainers. Which one should I… should I ping?
I'll ping the instrumentation containers.
**Donal O'Sullivan** 19:25 Yeah.
**Juliano Costa | Datadog** 19:50 And then I'll share those two links that, Shenoy shared, like.
So, hotel recommends one approach, and Spring recommends another, right?
**Shenoy Pratik** 20:14 Yeah.
**Donal O'Sullivan** 20:20 And this spring document is from… 2025…
**Juliano Costa | Datadog** 20:25 Yeah.
Instead of the Java instrumentation maintainers, I'll tag the Java Instrumentation approvers.
Because all the maintainers are also approvers, so I'll tag more people.
I'm… I'm writing like that, hey, would someone be able to help us out reviewing this PR?
We know that OTAL recommends one approach, and Spring recommends another.
Then I added the two links. Which approach do you see more on the, on the Java users. Would make sense to keep micrometer on the hotel demo?
Should I add anything else?
Any extra context, or… Is that enough?
**Shenoy Pratik** 21:47 I think that is enough, yeah.
**Juliano Costa | Datadog** 21:49 Cool.
Okay.
And then to help, I'll go to the… Java channel, and just, ping the link.
Okay.
Maybe Trask will have some time, I don't know.
Okay. So… I'll add that to the… the notes… Anything else?
By the way, let me… let me share… some… insights. So the, the, the… One of the contributors from Persys opened the PR forum.
For adding the purses dashboards to… to the demo?
And while I was testing, I noticed that… purses do not support, exemplars.
**Donal O'Sullivan** 24:16 Hmm.
**Juliano Costa | Datadog** 24:17 as we do not have many exemplars examples in either the hotel docs or, like, anywhere else, I felt that it would be a huge miss for the community, because, like, exemplars are cool, Concept and feature.
So we decided to close the PR, and maybe whenever purses have, exemplars have purses back. So then I, I said, hey, what if I just put my agents to implement, exemplars in purses?
So I didn't… I don't know Persis, I… yeah, I, like… I don't know the project, I just cloned the thing and said, hey, let's implement this, and it opened 4 PRs, I got 3 already merged, and just 1 to go.
I didn't learn anything, but, the… maybe we will have exemplars on the… on process, and, then in the next version, we will be able to have, to add that to the demo.
**Shenoy Pratik** 25:31 Once it is added to the demo, everyone will learn Persys.
Yeah. That's the benefit out of this.
**Juliano Costa | Datadog** 25:40 I mean, the thing is that, like, the problem is not… purses itself, I think the dashboards and the creation of the dashboards is pretty straightforward. The problem is that the code behind it, so, like, I don't know the project, I… I didn't know how to navigate. I just cloned one REPL, like, the Persys REPL, and asked my agent, like, hey, implement this, and he was like, no, it's not on this REPL. You have the plugins REPL, you have the shared REPL, and you have… There was another REPL, so it actually pulled all the repos and did all the work, so I was like, okay, yeah.
I still did some tests locally, because it was my GitHub handle, so I have a… I have a reputation, too.
To, to care about, but, but it's still, like, Yeah, I want to write about it, because… Like… even though I contributed and we now have exemplars in person, I don't think that's an ideal approach to take, because… yeah, I will never be, like, an approver, or a maintainer, or even a triageger at a process project if I don't know the project, like…
**Donal O'Sullivan** 27:08 Yeah.
**Juliano Costa | Datadog** 27:09 And, yep.
So, it's a… I think we are passing through a tricky… Time in the industry that we are… Understanding how to work with all those tools, so…
**Donal O'Sullivan** 27:26 Yeah.
**Juliano Costa | Datadog** 27:28 I'm happy that I'm… we… I'm happy that we were already involved on the demo before it, so we actually know the project.
Ugh.
Okay.
Ugh.
**Shenoy Pratik** 27:49 I'll keep an eye on the CI.
And if this also fails, I'll… Make some more changes, and then update.
**Juliano Costa | Datadog** 27:58 And, if that goes through, then we can merge, and then, rebase all the… All the other ones.
Cool.
Okay.
Okay.
**Donal O'Sullivan** 28:16 I can, I'll make a priority to review that, spring PR, so tomorrow. I'll see if they're… because I think I asked them about that build failure, so I think they made an update. I'll see if it works, and if it looks good, I can… Give my blessing.
**Juliano Costa | Datadog** 28:32 Cool, cool. I asked the folks from the Java, so hopefully we'll have some.
**Donal O'Sullivan** 28:37 Yeah.
**Juliano Costa | Datadog** 28:38 expert, insights.
from the hotel community. I feel that the hotel community would rather have the hotel approach.
But I think they will also… be the ones… That will know if the community actually uses more micrometer than hotel, and then they will just tell us.
**Donal O'Sullivan** 29:02 Yep.
Yep, sounds good.
**Juliano Costa | Datadog** 29:04 Cool.
Then, thanks everyone. See you next week.
**Donal O'Sullivan** 29:13 See you guys.
