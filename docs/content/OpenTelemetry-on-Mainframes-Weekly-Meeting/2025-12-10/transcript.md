SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2025-12-10
Duration: 23 minutes
Zoom Recording URL: https://zoom.us/rec/share/HTsj9xGSdIUhqmiBQGcat8UDWFfsYpH2t_G-VrYTac-MROXpmGpf2ZCSUn0lShy3.8Mvfhicg4C7Q1tPy
============================================================

## Zoom Recording Transcript

**Jim Porell** 01:12 Hello there.
**Greg Shriver** 02:05 Blue.
**Jim Porell** 02:07 Fair, Craig.
**Greg Shriver** 02:08 Thank you.
**Kai Kirsch** 02:09 So…
**Greg Shriver** 02:10 Hey, Kai.
Welcome on, Bal.
**Ambili Pallimakkal** 02:16 Thank you.
**Greg Shriver** 02:19 Hey, Andrish.
**Andrej Chmelo** 02:22 Hello.
**Greg Shriver** 02:23 Annen. Hello.
Hey, Anand.
**Anand Somasundaram** 02:42 Hey, Greg.
I'm not sure whether Rudigo's gonna join. He was traveling…
**Greg Shriver** 02:53 Yeah, we have some folks traveling as well.
And there's Richard. Hey, Richard.
**Richard Nikula** 03:03 Oh, well.
**atoulme** 03:10 Hello?
**Greg Shriver** 03:13 glue.
**atoulme** 03:15 Why am I on the wrong camera?
Yep.
**Greg Shriver** 04:27 More, huh?
**Morgan McLean** 04:34 Hey, everyone.
**Greg Shriver** 04:37 Hey, Morgan.
Wow, I think we… that's a record.
**Richard Nikula** 04:42 We're gonna say, pretty close, for sure.
**Greg Shriver** 04:45 Yeah.
**Morgan McLean** 04:45 to be a record for attendance, and we're actually, like, on a week where we're actually missing some normal… some of the usual attendees, so this is pretty great.
**Greg Shriver** 04:52 Wow. Yeah.
**Morgan McLean** 04:59 I only had one topic, if you want to get started.
**Greg Shriver** 05:04 Absolutely, yes.
**Morgan McLean** 05:06 Yeah, so mine is, I got in touch with the person at the CNCF who Rudiger and IBM have been working with on, getting us access to GitHub Actions runners, with mainframes.
They are still hashing out the contract details of IBM. I'm not part of that, and that's fine. And then, he said early in the new year, we'll be in touch and we can actually get those set up for OpenTelemetry.
So we'll revisit in January, but it seems like we're gonna get that, which is great.
**Greg Shriver** 05:42 So, it's… so… I'm trying to type and talk at the same time.
**Morgan McLean** 05:47 Yeah, I can't do either very well. Ruger has the specifics, because he's… I think he's involved in whatever IBM contract is going on. But, it's basically GitHub, the ability for GitHub Actions to use, I think it's IBM S390X infrastructure.
And so we could use that for builds and tests of various components.
**Greg Shriver** 06:08 Cool. Yeah, that's great.
Also, I think one of the other topics, which I don't know if we can actually address today, I'd prefer to have Rudy get here, or at least make sure that he's aware, was the schedule change.
**atoulme** 06:27 Hmm.
**Greg Shriver** 06:28 So, it looked like the survey that Angelica put out, that we could hopefully move this hour… move this meeting an hour early on… on Wednesday… an hour earlier on Wednesdays to be more…
you know, friendly to the folks in Europe.
**Morgan McLean** 06:45 Yep, and so if there's no objections, I can make that change starting next week, just let me know.
**Greg Shriver** 06:52 Well, should we make that change without Rudiga? Or, I don't know if Rudiga actually responded to the…
the survey… It's.
**Morgan McLean** 07:00 pretty essential. Let me, let me reply back to it and actually, like, like, at mention him directly, so make sure he gets a notification.
**Greg Shriver** 07:09 Sounds good. Yeah, I didn't see any… any other objections to your… to your note in the Slack, which… which is good.
**Morgan McLean** 07:15 Yes. So…
**Greg Shriver** 07:16 Okay, cool.
**Anand Somasundaram** 07:21 I had one topic.
Specifically for Morgan. There's an issue by the number 12177 on the hotel collector.
Can you give us an outlook on that?
**Morgan McLean** 07:38 Antoine actually works on the collector. Antoine, if you want to take a look?
**atoulme** 07:42 Yeah, what's.
**Morgan McLean** 07:44 I think it was 1217.
**Anand Somasundaram** 07:45 7, 7.
**Morgan McLean** 07:47 1277.
**Anand Somasundaram** 07:48 Yeah, 12177.
**atoulme** 07:51 Okay.
**Morgan McLean** 07:52 That extra digit makes a lot of sense. Yep.
**Anand Somasundaram** 07:54 I have a clue.
**atoulme** 07:55 1 cents.
Is it in Cultiv?
**Anand Somasundaram** 08:00 Yeah, this is like, you know, when you're adding extensions, it's not plug and play, it's more like you have to
The extension should be part of the build.
Itself. And we're wondering whether there's any… anything going on
The community to make that happen.
**atoulme** 08:22 Okay, so this is not related to mainframe, this is more of a design discussion about the collector itself.
**Anand Somasundaram** 08:28 Yeah, that's… yeah, it's nothing about to do with the mainframe.
How do we integrate extensions into the… as part of the hotel collector? Can we make it plug and play?
**atoulme** 08:41 Oh, Plug and Play here is doing a lot of work, because, you know, Plug and Play was coined as the USB original Promise in… this is a hardware component, and what that meant is that USB would be auto-discovered by the OS and somehow plugged into the bus, and made it possible for them to have the OS do some
low-level type integration. This is not the case of what you're asking for here. I think you're asking for a way to,
Integrate with another process at the compilation, outside of the compilation phase.
**Anand Somasundaram** 09:14 Yep.
**atoulme** 09:14 Extensions today are modules in Go that are compiled into the actual binary. This is available and distributed as such.
The issue that you pointed out is an RFC. It's a request for comments, meaning that it's not proposing a solution, but it's requesting for people
to share interest and put comments about whether they think a particular solution for extensions outside of the main compilation process would be available and meaningful for people. And I think, if you're interested in that, the first step to do is to go and comment and express interest for such a thing.
At this time, there is no way to do an extension mechanism that would be relying on external services or external processes for security reasons, mainly.
Also, because of the complexity of dealing with two processes is tenfold compared to running with one process. The type of integration we can think of could be based on networking, TCP socket type discussions, or could be based on shared memory, shared files.
or any other mechanism that are going to be available inside a shared boundary.
None of those things are being seriously considered at this time. There is no reason for us to consider those things, because it's actually fairly trivial to add another extension to the collector and to recompile the collector with this additional extension.
So, if there's a specific use case you're thinking of, that would be great to have you
Comment on the issue, explain a little bit where you're coming from.
And, yeah, we could really use more of that.
**Anand Somasundaram** 10:49 The use case is the customer has an extension, right, and we have a product using hotel collectors. How do we integrate this?
**atoulme** 10:58 Okay, but that's too vague. What's the extension doing?
**Anand Somasundaram** 11:02 It's a lot, too.
Access tokens, I guess.
**atoulme** 11:05 We have enough access token management solution as part of an extension.
**Anand Somasundaram** 11:10 Today. They're using something on… very proprietary, I guess.
**atoulme** 11:16 Okay.
**Anand Somasundaram** 11:19 And, how do we integrate with the product, if you have any thoughts?
**atoulme** 11:24 I think this is something that the RFC should be accommodating for, but I would say that the current OAuth extension that we offer for OF2 authentication
should somehow be sufficient for most of the use cases. If not, then this is something that we can expand. If you have a specific use case, such as, I don't know, would be a good one. Maybe you're using an actual,
hardware device that is performing the check by, you know, keeping the private key outside of circulation. You know, there's… I can't remember.
I remember that there's a… when I was working in crypto, we used to have this type of use case from enterprise customers, where there was actually a device dedicated to hosting the keys and performing signing and verification of tokens. If that's what you're thinking about, there are ways to do that which don't really involve the collector, but are done at the OS level.
if there's a specific use case in terms of, you know, support that is missing, I think it needs to be discussed at this of extension. But if you have a need for an extension that is going to be pluggable somehow.
even if you have an OAuth extension that is sitting there.
As an extension for this, it's half the battle, because…
you… the extension mechanism is extremely simple. All the collector does is start, stop, and makes the extension available so it can be cast as a particular type of object for specific components that are looking for them. So, other components configuration will be relying on the definition of that extension, such as by, you know, referring to it by ID, for example.
To load it at, validation time, when the… before the component itself is started.
to, add it to its life cycle, right? So…
Let's say you have an auth extension, you are going to have an authentication key under the OTRP exporter, for example. This authentication key can refer to the extension being registered as part of the configuration in the YAML, which will then load that up and use it when it's time to authenticate by casting it to be an authentication object.
That has some specific methods they can verify or append to the request the right, the right token information.
So,
Yeah, the boundary and the contract of an extension is very vague and very shallow on purpose, because extensions can be used for encoding, authentication, it can be used for marshalling, unmarshalling,
you know, you name it. So, you're gonna have to do a bit more…
legwork of pushing a comment on this particular RFC with your point of view and what you want. You can mention you discussed this in this SIG meeting. This SIG meeting is dedicated to mainframes, which are a type of hardware which, you know, going back to 60s, 70s, is going to be more of a shared server, that it can be shared with many customers.
schematizing, you know, it predates the idea of the personal PC. And we're working with, you know, the mainframe community to make it that OpenTechMindG becomes a first-class solution for this type of environment.
But for this type of discussion, you can participate in a collector's seek, which is happening on a rotating basis between, you know, APAC times, Europe times, and Amer times.
You can find the schedule of that under github.com slash opentemetry slash community. You will see in the table.
that we have different SIGs with different interests, and one of them is the collector. You'll be able to participate in those discussions there. You can also check out the OAuth extension, which is under the Contrib repository, OpenTeometry Collector Contrib.
you'll find it under Extensions, and that off, provider.
will probably satisfy things. I know it's something that Auth is very versatile, like, you can find 10 ways to authenticate people, apparently. So, we recently, as of, like, last 6 months, we've had more people show up and give us even more ways for people to kind of authenticate using auth.
So I'd be… I'd be, like, just interested to find out, like, if your customer really needs that custom…
Treatment for OAuth, when does it come in? Is it going to be an extension of the OAuth provider, or is it its own provider?
**Anand Somasundaram** 15:58 Yeah, let me dig into that, and also try and make a comment in that, for that issue.
**atoulme** 16:04 Cool.
**Anand Somasundaram** 16:05 Thank you.
**Greg Shriver** 16:12 Cool.
Any other topics?
Guy.
**Kai Kirsch** 16:25 Yeah, I thought minor one,
Let me quickly share my screen.
Maybe this helps. So I'm working, right, on reading a little bit about messaging systems.
And the, semantics, convention, right, for messaging systems, we have here defined a list of well-known,
systems, and they asked, basically, Shell, can we add, right, IBM MQ as well here, because it looks like it's, it's missing here.
And I think there's a question also for Anand and Ridiger, because I see, right, IBM is already setting this value in the, in the latest release, when they, when they're creating spans for, for, for,
MQ, and they are also setting then, right, basically, IBM MQ,
The name for the messaging system.
**atoulme** 17:19 Oh, cool.
Do you want to open a PR to add this?
**Kai Kirsch** 17:26 Yeah, if there are no objections, right, I would follow then, what IBM is already doing, basically IBM MQ, because I've seen, right, from different vendors, there's basically IBM.MQ underscore MQ, but I would follow then.
**atoulme** 17:39 The same convention view.
And always for me, but you might… so the semantic convention is a separate SIG, and…
You might hear from them a little bit more, in terms of what… please make sure you refer to that source of truth from the IBM NQ specification, and I don't think it will be a huge issue.
**Kai Kirsch** 18:03 All right. Thank you.
**Greg Shriver** 18:06 Yeah. So the next step, then, is… is, Kai, you're gonna draft the PR?
**Kai Kirsch** 18:11 Yep, yep, I'll work with you, Craig on.
**Greg Shriver** 18:14 Perfect.
Sounds good.
**atoulme** 18:23 I mean, IVMQ is not… it's…
tangentially related to mainframes, right? In my opinion, because you can run on Linux at this point, or whatever system. So, you… we actually have an IBM MQ integration that is available on the Java Contribository, if you're interested, which I've offered.
It's, allowing you to kind of monitor the health and metrics of a queue manager and its queues and whatnot.
I'm interested in getting more feedback from folks. It's just…
It's, frankly, needs more love, and there's some limitations about the approach, because we don't have a way to unregister a gauge or counter after it's been registered, so your queue manager might drop off, and then you still report its metrics as of its last point, where it started to report.
So I need to find a way to make that better, but…
We've been… been hitting data on some of the API and SDK specification folks who have been sitting on this for 2-3 years, and I'm trying to get there, but it's just taking a lot of work.
Not enough time to do it.
**Greg Shriver** 19:39 Makes sense, Juan.
Any other topics?
So, just an update from my side. I am still trying to…
get my doc PR. I did submit
I did submit a pull request, but I'm having…
personal issues, I guess, with, with being able to have it pass the EZCLA check.
And I think that has to do with, I thought it had to do with the wrong email address in the, in, in the…
in the repository that I used to draft the PR, so…
I'll work on that, and hopefully get that, get an update. I'm not going to share it now, because I probably…
I'm wondering if maybe the best way is just… is it even possible to delete the PR and resubmit the PR?
Is that a… is that a thing that's frowned upon, or…
**atoulme** 20:56 Oh, no, we don't care.
**Greg Shriver** 20:58 Nice.
**Morgan McLean** 20:58 frowned upon, and for easy CLA issues, it's probably the best path.
**Greg Shriver** 21:02 Okay, thank you.
Alright, so I will… I will work on that and hopefully have an update next week.
An actual PR next week.
**Morgan McLean** 21:18 Alright. Is that it for topics?
**Greg Shriver** 21:23 I don't have anything else. Anybody else?
Alright, cool, cool, cool.
**Morgan McLean** 21:32 Yeah, we can wrap it up. Alright.
**Greg Shriver** 21:34 So, let's wrap early. Thanks, everybody.
**Jim Porell** 21:36 Thanks, everyone. See ya.
**Anand Somasundaram** 21:38 Thank you.
