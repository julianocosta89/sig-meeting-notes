SIG: SIG Injector
Date: 2026-05-28
Duration: 20 minutes
============================================================

## Zoom Recording Transcript

**Nikola Grcevski @ Grafana / OpenTelemetry** 00:56 Okay.
**Bastian Krol** 00:58 Hey there.
To be honest, I'm not sure who will show up today. I think Jack and Michaela are out, and I'm not sure about Antoine.
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:12 Oh, okay.
**Bastian Krol** 01:14 That's what they said in the channel.
August.
Did you have any topics for today?
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:36 No, actually, I was away… Today is my first day back at work since last week, so… Oh, okay. I haven't had much time to look into anything, but…
**Bastian Krol** 01:48 Yeah. I guess… let's see if anyone else shows up, and otherwise, I guess we can… Nikola Grcevski @ Grafana / OpenTelemetry 01:56 I guess we made a release, 091?
**Bastian Krol** 01:59 Yeah, that was about Jack's fix to that lip C4. Yeah, exactly.
**Nikola Grcevski @ Grafana / OpenTelemetry** 02:06 Okay. Cool.
And death?
That's great. Okay.
Have you folks upgraded dash zero yet to this?
**Bastian Krol** 02:19 Not released, so I've just, upgraded our main branch, and all the tests passed, but we have not released it yet, later today or tomorrow, I guess. But I think that's… Nikola Grcevski @ Grafana / OpenTelemetry 02:34 It's gonna be the book, yeah.
**Bastian Krol** 02:36 Fine.
**Nikola Grcevski @ Grafana / OpenTelemetry** 02:43 There was an issue open that somebody, I don't know, I saw it, asking for… Declarative config.
I don't know if that… we can look into that. I don't understand it.
**Bastian Krol** 02:55 Sure, I've not looked into it… yet.
**Nikola Grcevski @ Grafana / OpenTelemetry** 02:59 We can look into that, since there's no other agenda.
Mmm.
**Bastian Krol** 03:05 That's a good point.
**Nikola Grcevski @ Grafana / OpenTelemetry** 03:09 Must have lost the email.
I thought we already spoke about a decorative config, but… support declarative config to override config.
**Bastian Krol** 03:30 Yeah, we certainly have talked about it. I'm not sure if we ever came to a definitive… Conclusion about the whole configuration approach.
**Nikola Grcevski @ Grafana / OpenTelemetry** 03:58 Not sure how this would work, but it's interesting.
So they would like the injector to be able to load a clarity config file which is deployed by OPAMP to override the current values.
**atoulme** 04:22 I hope.
**Nikola Grcevski @ Grafana / OpenTelemetry** 04:23 This for the… Collector, no?
**Bastian Krol** 04:29 I think that's the only component that currently uses this, shell.
basically, but I'm not sure if it's… If there are any technical reasons why it would be restricted to only the collector. I think it's worth considering.
But, I mean, he's not really talking about op-amp, is he, right? He just says that the declarative config file has been deployed by OpAMP to a specific… and then it's for the ejector, if I just read what is written here, literally, it wouldn't matter that op-amp has placed it, or whatever.
Puts a file on disk.
Hello, Antoine.
We were just looking at the… At issue 353…
**atoulme** 05:31 Yep.
**Bastian Krol** 05:31 We opened a while ago.
Talks about support for the collaborative config.
**atoulme** 05:39 Culture just, use the environment variable to point to a file, right?
**Nikola Grcevski @ Grafana / OpenTelemetry** 05:51 Yeah, I thought so. I thought there was an environment variable that you can just specify which file to pick up, so… Maybe that will work.
**Bastian Krol** 06:00 But is it the same format? Because, I mean, does the configuration file format that we have with the key values, is that supported by a declarative config?
**atoulme** 06:14 Definitely so.
Let me find it. Declative.
**Nikola Grcevski @ Grafana / OpenTelemetry** 06:18 This is if passing JSON YAML has performance implications, we could add… conf as a supported credit config file type.
**Bastian Krol** 06:29 Hmm… Nikola Grcevski @ Grafana / OpenTelemetry 06:30 dot com, what is that like?
**atoulme** 06:32 Hotel Configtal.
**Bastian Krol** 06:33 dot comf is at what we use, I think, right? Yeah.
**atoulme** 06:38 I mean, it says so from the top of this.
Discussion here.
It says, to get started, you save the fully configuration file as now.
And then you… Yeah.
**Bastian Krol** 06:55 Yeah.
**atoulme** 06:56 So.config file is a magic string, magic virtue set.
We should release… Not care.
Start with the right things.
**Bastian Krol** 07:10 But, I'm not… sorry, I don't…
**atoulme** 07:15 So, the injector config file.
Yeah. That's the ability to, allow environment variables to be injected into SDKs, right?
We can…
**Bastian Krol** 07:23 Yeah.
**atoulme** 07:24 One of them, is Hotel on.
**Bastian Krol** 07:28 Spotify.
**atoulme** 07:29 underscore far, which can point to a declarative config.
**Bastian Krol** 07:32 Yeah, I think he… the person from the ticket is asking for something different, which is to configure the injector via declarative config, not… So… Whoa! That's…
**atoulme** 07:47 No.
**Bastian Krol** 07:48 That would mean that we would need to build support for, for maybe reading YAML, or…
**atoulme** 07:55 No. Wait, that sounds a lot more work.
**Bastian Krol** 08:00 Yeah, yeah.
definitely not a small thing. And I know we have talked about it, maybe in passing at some point, but I don't think we ever documented a definitive stance on whether we ultimately want to support declarative config in the injector or not, or if it's out of scope.
**atoulme** 08:22 No, no, it's fine to use declarative config in the injector, because we just use the way it should be done, which is you set an var for the SDKs to load up a declarative config, but there is no such thing as a declarative config for the injector, nor are we interested in that. Just like the collector does not have a declarative config, or… OB does not have a declarative config, or…
**Bastian Krol** 08:44 Wow, because…
**atoulme** 08:45 Config is an SDK thing. It's meant for SDKs only.
**Bastian Krol** 08:49 Oh, okay, that's good.
That's good to know.
**atoulme** 08:53 If there is a misconception there, like… We should not have a YAML file for the injector, because we're going to increase the surface area for how much configuration we allow.
**Bastian Krol** 09:03 Yeah, yeah.
**atoulme** 09:04 it should be that simple. Like, this thing is just a trick, right? We're just loading some things and configuring stuff, and then we get out of the way as fast as we can. If you have to… if you have to parse a YAML file at every startup of the injector, you're opening a surface attack that I don't like. Have you ever…
**Bastian Krol** 09:22 Okay.
**atoulme** 09:23 Have you ever met the guy who invented YAML?
It is such a… it's a trip.
**Bastian Krol** 09:29 What's it?
**atoulme** 09:29 I keep calling once, and one guy shows up, he's like, YAML inventor, I'm like… What? Who are you? He goes, well, I'm making the rounds here because I'm the guy who invented YAML, and Kubernetes is not using it the way it should.
And he starts to tell me about his, his… is Quest to make YAML a full Turing programming language where any YAML instructions can do a HTTP fetch, or can execute.
**Bastian Krol** 09:57 And I'm like, buddy!
**atoulme** 09:58 What? Like, it's like.
**Bastian Krol** 10:00 Why?
**atoulme** 10:01 It's so much more powerful because you can have your YAML file start to do things, like, on your behalf, right? So, your Kubernetes config file starts to make it so you can fetch remote files from somewhere else, and I was terrified.
I was like, what I… no! But, okay, I mean, I guess… and he has, like, a complete working example in C.
And it's like.
Any language, because you can cross-compile, right?
And I'm like, okay, this is starting to be a bit, like, it's been half an hour.
So, no, no YAML. Messed up.
**Nikola Grcevski @ Grafana / OpenTelemetry** 10:37 I think, I'm looking here, and if I read between the lines… It says, if passing YAML has performance implications, we could add a .conf as supported declarative config type.
So, I wonder if they're just asking… maybe they don't know how to supply the, the OTEL injector config file, or the config DIR.
**atoulme** 11:01 Yep, I think that's what's happening.
**Nikola Grcevski @ Grafana / OpenTelemetry** 11:04 Because they're saying, like, we don't have infrastructure to build their own system packages, so we'd like to have a place where they ship these configs through OPAMP or a similar way.
**Bastian Krol** 11:14 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 11:15 pick them up. My guess is we just need to tell them that these things exist.
**atoulme** 11:21 You should start there, and then if you…
**Bastian Krol** 11:22 Then I read it wrong, maybe, yeah.
**atoulme** 11:24 If he meant it the way best he means it, then he can reply and say, no, I really want to do some op-amp to manipulate the injector config. In which case, the right answer is still, if you're going to manipulate text files with OpAMP, that's okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 11:39 Yeah.
**atoulme** 11:39 We don't need to be involved in that discussion.
Yeah. Like, you can have any external program on your machine can come and edit the config files of the injector, but there's… that's not a declarative config discussion.
**Nikola Grcevski @ Grafana / OpenTelemetry** 11:52 Yeah.
**atoulme** 11:53 Actually, pretty neat, we should have that. So the opam supervisor is a program that allows you to manage remotely files, and config files, specifically, on a host.
And I can see a bright future where we would allow a Open supervisor to go and change some config file that could be tied to… You know?
the injector.
Maybe, if we care.
Is there a use case for that? Sure.
**Nikola Grcevski @ Grafana / OpenTelemetry** 12:21 Yeah, I can ask a question.
**atoulme** 12:24 I think the best use case would be that we tell people to use the YAML file for declarative config for everything moving forward, and then that's what people should rely on.
F… Let me share something.
So that's KubeCon London.
In case you think I'm not… Serious.
That's… that's… that's… that's a real purpose.
**Bastian Krol** 13:36 reviewed.
**atoulme** 13:38 And that's NJ from, collector.
**Bastian Krol** 13:40 Okay…
**atoulme** 13:43 So, that happened. I have proof.
**Bastian Krol** 13:46 Very interesting, yeah.
By the way.
**atoulme** 13:53 Yeah.
**Bastian Krol** 13:55 You said it on. You, you mentioned in, in Slack, the observability.
**atoulme** 14:00 Oh, yeah.
**Bastian Krol** 14:00 project updates, which event did you have in mind specifically? I'm a little bit confused by the different KubeCorns and which one's up next, and…
**atoulme** 14:09 Yeah, this is a good venue, right? So, Well, yes, there are multiple coupons this summer, and I think the CFPs for them must be closing by now. One is in Japan, I think I got rejected for all my talks.
**Bastian Krol** 14:21 clear.
**atoulme** 14:21 India, might be a bit much.
But for you guys, I think it would make sense to try to attend and present at the one in Salt Lake City, which is in November.
The… there are two CFPs. So the way it works is that there's a main event.
And, first, that CFP is going to close on the 31st of May, so you have a few days left. And the bar for that is pretty high, because you're going to, to kind of compete for attention and time with Kubernetes projects and every other CNCF project.
And I think at the same time, there's a co-located event. So, actually, there's two things. There's one that you really need to go if you're coming.
One is the collocated event, which is the holiday. Holiday is just a one-day event.
**Bastian Krol** 15:05 that.
**atoulme** 15:06 you can be part of that. It's more open to observability, the use cases are more narrow, it's a good shot to get into this.
And, finally, there is a maintainer summit.
If you've never been, it's the day… that's Sunday, so it eats up your weekend.
**Nikola Grcevski @ Grafana / OpenTelemetry** 15:23 Beautiful.
**atoulme** 15:24 But it's, it's a day for kind of meta-discussions about how to maintain the project. There usually is an hour where we talk about OpenTeometry, where maintainers, kind of, can come together.
And…
**Bastian Krol** 15:36 Okay.
**atoulme** 15:37 That's usually what…
**Bastian Krol** 15:40 Interesting. Yeah, I need to take a look if I can do something in the US.
1, 2, yeah.
**atoulme** 15:49 And your changes augment, if you have… I mean, as, you know, first, no vendor… no product pitch, no vendor-led stuff, like, it's really meant for community, and you… I think your chances increase if you're able to kind of have two people from different companies, so… If you both want to go for it, I think that would be cool. I think, bestie, if you want to make an update on the injector, you have the most experience.
Clearly worked the most on that, Nikola is the close second, and then you would be able to, kind of.
Talk about a bunch of things that have been happening there.
**Bastian Krol** 16:26 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 16:27 Yeah, I've found that two people from different companies are, usually get better chance, that's for sure.
**atoulme** 16:37 Yeah.
Transparently, I submitted a request for a proposal for me and Michele to go talk about the new packaging scene.
Okay.
**Bastian Krol** 16:46 Nice.
**atoulme** 16:47 That's trying to cover different angles.
**Bastian Krol** 16:51 Quick clue.
**Nikola Grcevski @ Grafana / OpenTelemetry** 16:54 We could submit something, like, I was thinking about it a little bit… Mixing up… BBPF and injector stuff.
Kind of.
Instrumentation just showing how it could be done.
I don't know if that… We can… we can try that.
**Bastian Krol** 17:16 Yeah To be honest, I'm not… not… I… would need to think about if I even want to travel to the US, just… just for talk, That's risk. Yeah, but…
**atoulme** 17:39 You know, I think… Nikola Grcevski @ Grafana / OpenTelemetry 17:40 You're absolutely right, yeah.
**atoulme** 17:42 That's done. I completely get it.
**Nikola Grcevski @ Grafana / OpenTelemetry** 17:43 Yeah, yeah, I get it. Yeah.
**atoulme** 17:46 And if… if that doesn't happen, then, it's too bad, and… Nikola Grcevski @ Grafana / OpenTelemetry 17:51 I mean, I could submit it, Oh, still get exposure. We can still get exposure. I mean, if we get accepted, doesn't mean we'll get accepted. It's really hard. It's really hard. I've gotten so many rejections that it's, like, a fluke when you get accepted.
So…
**atoulme** 18:10 very difficult.
But.
**Bastian Krol** 18:12 Yeah.
**atoulme** 18:12 you guys have a better chance because you're actually doing the work, and I mean, I've been on those type of committees when you review talks, so you have about 2 weeks to review, like, 70 talks. Each person does that.
**Bastian Krol** 18:22 Yeah.
**atoulme** 18:23 It's a bit of a difficult discussion, because you have a lot of, like… so you have multiple categories you need to vote for, right? You have, like.
Is the content good? Is the offer someone who's part of the community you can recognize is worthy of presenting? Is, is it in line with the, spirit of what the conference should be about, and things like that. You get a lot of developer advocates for just chipping in, like, spreading whatever.
Yeah.
**Bastian Krol** 18:53 jam.
**atoulme** 18:53 Lots of people who are just going to present a pet project, so, you know, sometimes you get, like, IBMers, just 2 IBMers, and they present 6 different things, and you're like, it's just… come on.
So, yeah, I think you would have a, in my opinion, a better chance than most to get in, because you can speak to the value of the project.
And you would… you would strain to, like, product lines as much.
But, yeah, I get it. Also, like, Yeah, you could put your name and change your mind later.
**Bastian Krol** 19:29 Yep.
**atoulme** 19:34 Cool.
Is there anything else?
**Bastian Krol** 19:39 I don't think so… Nikola Grcevski @ Grafana / OpenTelemetry 19:48 Huh?
**Bastian Krol** 19:51 Okay.
I guess. Can't quite a date.
**Nikola Grcevski @ Grafana / OpenTelemetry** 19:55 Yep.
**atoulme** 19:56 Bye.
**Nikola Grcevski @ Grafana / OpenTelemetry** 19:56 See you guys later.
Bye.
