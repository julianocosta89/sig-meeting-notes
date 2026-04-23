SIG: Developer Experience SIG Meeting
Date: 2026-04-22
Duration: 49 minutes
Zoom Recording URL: https://zoom.us/rec/share/S26N33y6qN5bfv7KdJUNHB4geOdrpptnFre6v3fQ0Oo2ENvM3ml0g1QPGt-jvrBZ.MLTbrADa2mFjEbzY
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 00:10 Hello!
**Johanna Öjeling** 00:15 Hello! Morning.
**Juliano Costa | Datadog** 00:18 Morning. How are you?
**Johanna Öjeling** 00:20 I'm good. How are you doing?
**Juliano Costa | Datadog** 00:24 Good, good, good, good. Busy.
That's normal. Yeah.
**Johanna Öjeling** 00:33 Do you have any, Vacation planned for the summer or spring.
**Juliano Costa | Datadog** 00:41 I think just me.
Now I need to double-check that. I do have, but I… I don't remember when.
**Johanna Öjeling** 00:51 Yeah. Thank you, if you have something to look forward to when it feels too busy.
**Juliano Costa | Datadog** 00:58 Oh, no, it's just June.
Yeah, it will take a while.
Anyways, yeah.
It's good.
So…
**tristan** 01:16 Are you in an office, or is that your home?
Truly. Me? Yeah.
**Juliano Costa | Datadog** 01:21 Yeah, that's my… my flat.
**tristan** 01:24 Oh, okay. Kinda works like a… So…
**Johanna Öjeling** 01:27 Yeah, it looks really nice.
**Juliano Costa | Datadog** 01:29 Yeah, I bought at, Tebu. There's a sticker that I can put on my wall, so it really… Yeah, it is.
**tristan** 01:41 Is that weird?
**Juliano Costa | Datadog** 01:43 3, 4 meter sticker row, and I think I bought, like.
5, so you're just, like.
**tristan** 01:51 the damage.
**Juliano Costa | Datadog** 01:53 stick them together. Yeah, it looks good.
Cool. So, first of all, congrats on the… on the Skyscanner blog post.
**Johanna Öjeling** 02:13 Oh, yeah, thank you.
**Juliano Costa | Datadog** 02:15 one.
This one is really good, yeah.
**Johanna Öjeling** 02:20 It is, yeah, I'm super happy that Neil was able to share so much information, and he was also very responsive.
when we asked for more, like, diagrams and snippets, so I think it's, super cool for, OpenCollector users out there to, yeah, see the actual, configuration.
**Juliano Costa | Datadog** 02:44 Totally. I would even say, not just, like, collector users, but also the…
**Johanna Öjeling** 02:52 like, instruments.
**Juliano Costa | Datadog** 02:53 Regular users, yeah, yeah, yeah.
**Johanna Öjeling** 02:54 -
**Juliano Costa | Datadog** 02:55 Like, how to use Hotel as a platform?
**Johanna Öjeling** 02:59 Yeah.
Exactly, and illustrating with their Java instrumentation how they build, a base image from the agent, and so on. So, yeah, I think it contains a lot of useful information.
And, yeah, now these, These posts that have already been published will be added as reference implementation, so that's nice.
And, there was, a message in the Slack channel also.
in our Slack channel, by Dan Gomez Blanco, who posted about, like, adding new blueprints or adding new reference implementations going forward, so he took inspiration from, the blog post we have already written in.
Yeah.
The structure, of these.
So yeah, I think that's pretty cool that, yeah, our blog post will, you know, serve as the first, reference implementations.
**Juliano Costa | Datadog** 04:19 Do you know… Do you know how that will work?
**Johanna Öjeling** 04:27 I, didn't know before, looking into that PR, but as I understand it, they will… like, there have been a couple of pages added on OpenTelemetry I.O. presenting what is a blueprint and what is a reference implementation, and, When organizations want to contribute, a reference implementation or telling their story, then they will open a PR in I guess it's open to the MetroIO repository, and they can… submit information, whether they would like to write the reference implementation themselves, and then they follow this template, or if they need help with writing it, and then, I suppose.
That could be solved with… in a similar way as we have done with interviews, and then we write the post, and involve them for review.
**Juliano Costa | Datadog** 05:33 Okay.
Yeah, I just wonder, because I think the idea of having blueprints… was to have something that is more, how can I say? Like, current, and people can actually go back and update with new stuff that they are, using and changing, so I don't know how that will actually, work in real life, still.
**Johanna Öjeling** 05:57 Yeah, interesting. It is, yeah, and actually, yeah, so it was stated, you're right, that the blueprints will stay… like, relevant and be updated, whereas the reference implementations may become, like, obsolete. They won't be updated, I think, because they are organizations. But there was… a PR… I think this is adding the first reference implementation, so we can… Sorry, the first blueprint, to get an idea of what the blueprints will look like, and then there are the reference implementation, too.
Kind of illustrate how… how that looks like in real life.
**Juliano Costa | Datadog** 06:46 Oh, okay. I'll… I'll open here. I think we have, yeah, the preview.
I'll take a look.
Okay, so, yeah, from what I can see, it's basically, A blog, but it… it will be updated, and Yeah, I wish there was… There were more drawings, and… Thank you.
Architectures, as we did in the blog post.
But keeping those also up-to-date will be a pain.
Yeah, that's…
**Johanna Öjeling** 07:29 Very good point. Yeah, that's, good feedback, because Having some diagrams would help.
Readers understand, in a better way.
**Juliano Costa | Datadog** 07:41 We have.
Nice, nice.
I saw that the… regarding the Atlassian thingy, I don't… Tristan, that… Did that happen?
the Atlassian interview? I don't remember.
**tristan** 08:02 Yeah, it did. That was a while ago. That's the problem?
**Juliano Costa | Datadog** 08:06 Yeah, I don't…
**tristan** 08:07 I have my notes, and I have answers, because I gave them follow-up questions, I can send you, Well, yeah, the recording… I'm trying to remember how we recorded that, if it was… My recording, or your recording, or…
**Juliano Costa | Datadog** 08:24 Was… was it a classion that, that… the one that you started recording, and then I… I finished?
**tristan** 08:35 Yeah.
I think so.
**Juliano Costa | Datadog** 08:38 Okay, I think I shared with Johanna this one.
**Johanna Öjeling** 08:42 a skyscanner.
**Juliano Costa | Datadog** 08:43 Okay, Skyscunner.
**Johanna Öjeling** 08:44 The first part of Dinky was, like, Google Recorder, and then second video.
**tristan** 08:51 Okay, well, I have a… recorder of Atlassian. It was only 40 minutes, so I thought it was the split one, but yeah, I can send you that recording.
**Juliano Costa | Datadog** 09:00 I think Atlassian. Atlassian was the first one, wasn't he?
**tristan** 09:04 Yeah, it might be.
**Juliano Costa | Datadog** 09:05 Yeah, because I think the first one, we didn't have a proper,
**tristan** 09:10 Yeah.
**Juliano Costa | Datadog** 09:10 way of recording, and we didn't want to record on the public,
**tristan** 09:14 Right, we thought, yeah, we were being too slick.
**Johanna Öjeling** 09:17 Yeah. Okay.
**Juliano Costa | Datadog** 09:18 And Tristan recorded on his.
**tristan** 09:23 Just make everything public, it's easier.
**Johanna Öjeling** 09:28 But then, I will tag you in that GitHub issue, Tristan, where community member, Brooklyn, yeah.
**tristan** 09:35 Yeah, it's kinda… interesting.
**Juliano Costa | Datadog** 09:39 maybe not to… to share the recording in there, maybe we could add a link, in, in, in our, DevEx SIG meetings. I have a tab for recordings.
**Johanna Öjeling** 09:53 Oh, yeah.
**Juliano Costa | Datadog** 09:54 Drop, Densk, and Adobe.
I will actually remove Adobe, because that was already published.
And we can maybe add, Atlassian gear.
**Johanna Öjeling** 10:07 Yeah, that's a good point.
**Juliano Costa | Datadog** 10:10 And I'll just tag, yeah.
I like that. I'll take, Tristan.
**Johanna Öjeling** 10:18 Great. Then… I wrote… Ask.
The person to give me their email address, so I can show, Cool. Documentation. Please.
**Juliano Costa | Datadog** 10:42 Awesome.
**Johanna Öjeling** 10:47 Then there is also the Grok blog post that I have a draft of, but it's a bit unclear how Andreas wants to proceed, because he moved over to NVIDIA, And he wants approval from Grok, and he found a person I could reach out to, but they haven't responded.
**tristan** 11:12 Who's the person?
**Johanna Öjeling** 11:14 Let me see…
**Juliano Costa | Datadog** 11:20 Because you worked there, right, Tristan?
**tristan** 11:22 Yeah, briefly.
**Johanna Öjeling** 11:27 Maybe… Oops, let me see if I can find…
**tristan** 11:31 Just in case it's someone I can ping, I don't know.
**Johanna Öjeling** 11:34 Yeah, the… K. Kosich.
**tristan** 11:43 Hmm.
**Johanna Öjeling** 11:44 Do you know who it is?
I shared the, the Google Doc and wrote an email, but I didn't get any reply.
**tristan** 11:57 Pretty sure everybody I knew ended up at NVIDIA.
I thought all that.
I ended up at NVIDIA, but I guess not, so… that's…
**Johanna Öjeling** 12:05 Yeah, yeah, or if you want to ping him, or yeah, leverage your connection, to move forward, then just go ahead.
**Juliano Costa | Datadog** 12:17 This one is also nice, one engineer, tough.
Yeah. 12,700 collectors.
Okay.
**tristan** 12:27 It was a cool setup.
**Juliano Costa | Datadog** 12:29 Yeah.
**Johanna Öjeling** 12:30 Yeah, and yeah, that's cool, and I also think this use case is interesting, because how they work… how they use Prometheus exporters, with the UTA collector, because, yeah, all of the infrastructure metrics, right, they need to collect, so it's, yeah, it would be nice to get the story out there for others to learn from.
**Juliano Costa | Datadog** 12:52 And also that they are using OTAP.
So…
**tristan** 12:58 Yeah, yeah.
**Juliano Costa | Datadog** 12:59 Moto Arrow.
So that, that's…
**Johanna Öjeling** 13:01 That's so cool.
**tristan** 13:03 Yeah, take a look.
**Juliano Costa | Datadog** 13:05 Okay, yeah, If, I don't know, can I find them on LinkedIn, and I can maybe bug a lot of people until I get an answer?
**Johanna Öjeling** 13:21 Yeah, I don't know, actually, what's the name of K. Kosich, maybe?
Let me see if there are to tap you some of the same.
Nope.
**Juliano Costa | Datadog** 13:33 Is it a semiconductor manufacturing, Tristan? No, right? It's an AI company.
**tristan** 13:41 Yeah, what did… what did you find?
**Juliano Costa | Datadog** 13:43 On LinkedIn, there is a semiconductor manufacturing, there is Grok Health.
**tristan** 13:50 Oh, weird.
**Juliano Costa | Datadog** 13:52 But, not the AI one. It's… funny how people do not Google before creating their companies, like…
**tristan** 14:04 Yeah.
Oh, weird.
**Johanna Öjeling** 14:09 I think I actually found the K. Kosich, Kelly Kosich, who's head of legal.
**tristan** 14:19 It is the semiconductor one.
**Juliano Costa | Datadog** 14:22 Okay.
**tristan** 14:23 Even though right now they're just a cloud for AI, because NVIDIA, like, owns all the… Chip stuff.
But, whatever.
**Juliano Costa | Datadog** 14:33 Okay, so there are… There are folks here.
**Perk (Marcin Stożek) | Elastic Ingest** 14:39 I have this funny story. At some point in my career, I was, in my city, which is very local, I was, I was driving, you know, on a street and saw the company that struck me, and I thought, like, okay, this is a domain name, so I went to this domain name, because the name was as a domain name, you know? I went there, and it was, like, this very cool startup from Amsterdam or something, and I was like, oh my god, okay, that is interesting, so… I gotta call those guys, so I called the local office, and the local office was not the same company, that was a hairstylist.
**Juliano Costa | Datadog** 15:11 Okay.
**Perk (Marcin Stożek) | Elastic Ingest** 15:12 So I was unsuccessful.
**Juliano Costa | Datadog** 15:28 I don't have… any connection in… Like, in common.
**tristan** 15:40 Yeah.
**Juliano Costa | Datadog** 15:41 But, well, let's try… So I'll try to… Johanna, will you try to… to reach out to Kozic?
**Johanna Öjeling** 15:54 Yeah, I'll, I'll follow up on my last email and, Let's see if I can… the reply. But yeah, at the same time, I think, Tristan, if you can, also match Andrea, so yeah. Yeah. Great.
Then we have Kiko.
**Perk (Marcin Stożek) | Elastic Ingest** 16:26 Yeah, yeah, as for Kickloak, I, I've downloaded the recording, so it's secured there, and I started working on a local draft.
There's some… Well, a lot of useful information, like, as we are well out there, so that is going to be, I think, very nice blog post. That being said, I cannot work for it for another, like, two weeks, so I'll start at the beginning of May, so I'll share then at that time, if that's okay.
Also, I've moved to the, to… to my doc, but then I saw that there is another… another doc, I believe, that we keep all of those interviews, right? Like, you, Anna, you shared with me. So, should I… should I move the blog post, there, or maybe I can work with, you know, Alex and Martin on the one that I've created and then copy it over? Like, what do you prefer?
**Johanna Öjeling** 17:24 Yeah, up to you how you want to… if you want to prepare it, first in another document, but yeah, then when you feel ready, I think it would be nice to… Perk (Marcin Stożek) | Elastic Ingest 17:34 Yeah, fair enough.
**Johanna Öjeling** 17:35 To get it into.
**Perk (Marcin Stożek) | Elastic Ingest** 17:36 Thanks.
Yeah, I just… I just have it ready, so I don't want to, like, to, you know, like, Back and forth, too many, too many times.
**Juliano Costa | Datadog** 17:46 But… Perk (Marcin Stożek) | Elastic Ingest 17:46 I think you've all been added there.
So…
**Johanna Öjeling** 17:52 Yeah, then I think you can, yeah, move it over to the common document, and then we can all add our review comments, because then we can also see.
**Perk (Marcin Stożek) | Elastic Ingest** 18:02 Yeah.
**Johanna Öjeling** 18:03 Restaurants look at.
**Perk (Marcin Stożek) | Elastic Ingest** 18:05 Farewell, yeah, good idea.
Okay, Tristan, if you've sent me your email address, I can add you, or… If you're interested, of course.
**tristan** 18:35 Okay.
**Juliano Costa | Datadog** 18:45 Looks like, Kosic, from Grok is, like, the new Apple CEO, like… not existing on LinkedIn.
Okay.
**Perk (Marcin Stożek) | Elastic Ingest** 19:08 I have one more thing I wanted to show you guys.
Which is the thing that I was showing, you know, around at, at KubeCon to a couple of folks, and, and, and, I think, I think you might be interested. So, I'm just looking for, for your thoughts, you know? I, I, I, I saw this on the, OpenSeek, I think. This is, This is a thing that I was obviously VIP coding, not doing it myself, as, you know, everybody does today.
I think. So let me show you what I wanna… to show you. So, there is this thing that I called OPAMI, and OPAMI is this thing that I think is missing, which is a UI for a collector.
So… you know, like, protocol, you obviously can configure it through file, right? Everybody does that, and then through opum, but maybe, like, I thought that for the developer, especially, like, if you have something locally running on your desktop, then, there's this… very nice tool called, SyncSync, which is very similar in a way. SyncSync is a thing that can sync files between two computers. It's like Dropbox, but without, without a server, you know?
And the very nice feature of that, like, that I found very much useful for the past, I think, like, 15 years now, is the web UI for it. So that's a Go application that works, you know, as a server, but then there is a web UI for configuring stuff.
So, I thought, like, okay, we should, we should just do the same.
And, and I have something already working.
So, obviously, this shows you the, you know, all of the pipelines that are there, and the configuration, right, if you go into there, but the important part is that you get all of those metrics as well, so you know how many, you know, data is going through each component here, right? And if the pipelines are working.
at all or not, right? And then the end goal is to provide the Configuration, so that you can configure the pipelines, change the components that are there in the pipelines, and whatnot, and also see the status.
Of the saying, status of your collector.
Every component that is available, right? And so on and so forth.
And then the killer feature, that I think it's a killer feature, is that maybe you're not that much… into web UI, so why not just using the terminal UI for this, you know? And if you want to see the metrics for the infrastructure, just go and see the metrics for the infrastructure. Like, I need to figure out, I think, better UX for this page, for example, but that's the general idea. Like, UI for collector that is web-based, or the terminal-based, so that you don't have to go into the config file if you don't want to, right? So that you can have the nice visibility. So that's a very, very short demo. It's not open source yet. I have I have it literally on my computer only right now, but I'm, you know, like, thinking about, making it open source.
Early this morning.
**Juliano Costa | Datadog** 22:16 put in a… please put in a repo. If your computer dies, you lose all the work.
**Perk (Marcin Stożek) | Elastic Ingest** 22:22 Oh, sure, yeah, yeah, fair enough, yeah, yeah, so it's there. It's actually, it's actually, you know, because I use the SyncThink thing, it's actually there, distributed within my local network, right? But, other than that, yeah, yeah, it needs to end up on GitHub.
**tristan** 22:36 I have…
**Juliano Costa | Datadog** 22:38 I have one question. Is the opum part working? So I can… can I edit the running collector with OPUMI?
**Perk (Marcin Stożek) | Elastic Ingest** 22:46 So you cannot… you cannot edit it right now. It connects through OPAM, so it should be possible. It should be possible to change the configuration. I am at this phase when I'm only showing you the running config and the monitoring stuff, but that is the obvious next step.
To, yeah, to be able to change the config. Yeah, yeah, definitely.
**tristan** 23:06 I like the… the UI. Have you looked at ZPages?
**Perk (Marcin Stożek) | Elastic Ingest** 23:11 Z pages UI, you mean, or ZPages what exactly?
**tristan** 23:16 The UI for the collector?
It didn't… HTTP endpoint you can hit on the collector to see.
**Perk (Marcin Stożek) | Elastic Ingest** 23:26 To see the Z pages there.
**tristan** 23:28 Yeah, it's called Z-Pages?
**Perk (Marcin Stożek) | Elastic Ingest** 23:31 So I think I was at the Z pages, but I think it's different, isn't it?
**tristan** 23:36 I think it's similar, not the same, because you have, like, op-amp stuff, but it has, like, pipe… running pipeline stuff, and traces coming through, and… but its UI is much more, basic, and what's the word for it? Arcane? I don't know.
**Perk (Marcin Stożek) | Elastic Ingest** 23:57 Yeah, yeah, that's a fair call. I always thought that the Z pages is rather… Like, a monitoring for very internal stuff.
of your collector. Here, I think… I think I target the higher level, but maybe I'm mistaken. Maybe I need to figure, like, go and dive deeper into the Z pages itself.
**Juliano Costa | Datadog** 24:18 I want to play around with the pages now, I wasn't aware of that.
**Perk (Marcin Stożek) | Elastic Ingest** 24:21 Yeah.
I know that there is a UI for the pages. Oh, yeah, let's do it.
**tristan** 24:30 Yeah, this could be, like, an updated replacement for ZPages or something.
**Perk (Marcin Stożek) | Elastic Ingest** 24:35 Okay, yeah, I'll dive into that. That's a good call.
**Juliano Costa | Datadog** 24:40 Nice.
**Perk (Marcin Stożek) | Elastic Ingest** 24:41 Thanks.
**Johanna Öjeling** 24:44 Yeah, cool, project. Let us know, if or when you, put it, onto the top, and… Yeah, definitely.
**Perk (Marcin Stożek) | Elastic Ingest** 24:55 Yeah, now the hard part, so, like, push yourself to just, you know, move it out, you know?
The last mile.
Okay, cool, I'll keep you updated, then, on the… on that.
**Juliano Costa | Datadog** 25:10 Cool.
**Perk (Marcin Stożek) | Elastic Ingest** 25:11 Thanks.
**Juliano Costa | Datadog** 25:13 I think… Thanks, Tristan, for writing the recording.
I think you also wanted to… Yeah, you have it here on the agenda already. What to do next? I think I briefly discussed that with Johanna in a meeting that I think was just the two of us, and I mentioned that you wanted to do some… API and SDK stuff, right?
**tristan** 25:43 Maybe, I think we should consider it and try looking again at if there's work there we could do, so it doesn't… yeah. It's sort of more of a… It's a possibility, but we gotta figure out if there's things there that could use our focus, or if there's something else, or what…
**Juliano Costa | Datadog** 26:07 I, I feel… Honestly, I don't know, like, when I use the demo, I… I've… I kind of feel that I'm a OpenTelemptry customer zero, playing around with the new stuff.
And… even though I'm working with Hotel for four and a half years, I still feel that our docs are not ideal.
**tristan** 26:37 Hmm.
**Juliano Costa | Datadog** 26:38 So… like, the new, config file. It's a.
**tristan** 26:44 Oh my god.
**Juliano Costa | Datadog** 26:45 they released, they, made, some noise during KubeCon, great.
I don't know how to configure telemetry SDK, attributes, like, resource attributes. I check the docs, check the README, like, the READMEs, they, they are awful. And…
**tristan** 27:05 Yeah.
**Juliano Costa | Datadog** 27:05 I'm like, how can I… Maybe… what I'm trying to say is that maybe we should try to… take a different route here. So instead of Instead of battling the things that are already released and up, and then finding where the users are struggling, maybe we could go the other way around.
and make sure that the new things that we are developing and shipping are just marked as stable and consumable for end users whenever there is X, Y, and Z set. So, like, for a component to be marked as this table, you need to have a doc page, you need to have examples, and you need… whatever. Like… like, basic stuff.
I think we had something for… for the… for the… for hotel, but, I think it's just a guideline and not, like, enforced.
But yeah, this is, like, my… my thoughts here, but yeah, I… I don't know exactly if it… if it's under developer experience, or contributor experience, or, I don't know, GC?
**tristan** 28:27 But yeah, I just looked… I was curious, so I went to… The first page under… Languages API SDKs, then there's SDK config, so I click on SDK Config, go to General, and the first thing it gets me is all the… environment variables.
When we're supposed to be using the configuration file now.
So… That would be… and there is declarative configuration under there.
**Juliano Costa | Datadog** 28:54 Yes.
**tristan** 28:55 further down, and not clear that that's what you should use, or that… and then… oh, it only says Java is supported, I'm pretty sure that's wrong, but the…
**Juliano Costa | Datadog** 29:07 Yeah, it is… well, that's the thing. Alex Bolton contributed to the demo in a Go service.
And I was running the demo.
yesterday, and I found out that the service that is configured with the declarative configuration is not emitting telemetry SDK.
So, it's not saying that it, like, it is OpenTelemetry, the SDK version, and whatever.
**tristan** 29:35 So you wanted to add the view.
**Juliano Costa | Datadog** 29:37 And then I was like, okay, yeah, that's easy to solve, I just need to come here in the resource and say, capture this, but… like, I don't know what is the format, how we should… how is it called, or whatever, so yeah.
**tristan** 29:55 Agreed.
**Juliano Costa | Datadog** 29:57 Yup.
**tristan** 29:59 Interesting.
**Johanna Öjeling** 30:00 What's your, idea, Juliana, for how we could help?
**Juliano Costa | Datadog** 30:09 So… when we… I think when Tristan proposed the SIG, the idea was to tackle SDK usage, and, like.
when we thought about developer experience, we were thinking about folks using the SDKs and the APIs.
when we ran the survey, we found out that people were actually complaining about the lack of documentation on how to use the collector in production, and that's how we set up the interviews and everything, and then all the blog posts that we are releasing now.
but my, my point is… the SDK and the APIs Are complex, because we do not properly document the things that we can do.
So, is it, like, a developer experience It is a bad developer experience whenever using it, because it's complex, or because it's not documented.
And… when we think about AI nowadays, like, the better the implementation, the better it can actually implement this stuff. I know that AI can also read the code and find out about it, but yeah, I don't have, like, A proper idea of what to do next.
But…
**Johanna Öjeling** 31:41 But yeah, that's interesting, and you mentioned, stability, because I'm currently helping a co-worker on the, on stabilizing the Prometheus exporter in the SDKs, and… then there are some guidelines for when… when it's considered stable, and then, the Prometheus hotel interoperability say they're also working towards stabilizing the Prometheus receiver in the collector, and I just… I found… let me see if I… And find that link, because then there are some, like, documentation requirements that we are looking at, a certain, like, checklist.
But I wonder if, yeah, if there is something similar for SDKs, what that is, or, like, if there isn't, if we could help, Create those guidelines?
Or help identify where the current gaps are.
**Juliano Costa | Datadog** 32:57 What do you think, Tristan?
Because… Again, if we go the docs and, like, And even the spec path, we will derive again from the SDK and the API, which was the initial,
**tristan** 33:17 VIN.
**Juliano Costa | Datadog** 33:18 idea of the SEC. So, yeah, I'm curious to hear what you… you think.
**tristan** 33:26 Mmm… Yeah, I mean, that… That's certainly where I wanted to focus and think there needs to be focus, or have thought for years.
And there is… there's a Doc SIG, right?
**Juliano Costa | Datadog** 33:46 Very slow.
**Johanna Öjeling** 33:47 Yeah, communication sake?
**Juliano Costa | Datadog** 33:49 Yep.
comps.
**tristan** 33:52 open.
Oh, those are separate?
**Juliano Costa | Datadog** 33:55 No, it is… I think comms goes, Docs is under them, yeah.
**tristan** 34:02 Excellent.
**Johanna Öjeling** 34:03 Exactly, like, the OpenTelemetry I.O. docs, but not docs.
like, not the, like, GitHub readme, so…
**tristan** 34:11 Right, right.
**Johanna Öjeling** 34:12 For individual, projects.
**tristan** 34:13 Hmm.
I was wondering, because, I mean, they're probably doing a lot, versus just focusing on docs on the website, so… I just don't want to overlap with another SIG too much, or at all.
**Juliano Costa | Datadog** 34:31 But one thing that I always discussed with, severing was that, the docs team cannot document everything.
**tristan** 34:41 Right.
**Juliano Costa | Datadog** 34:41 They need the maintainers, and whoever is driving the features on the… on the programming level language, on the collector level, so, like.
them to actually come and contribute to the demo. To… sorry, to the…
**tristan** 34:59 To the dogs.
**Juliano Costa | Datadog** 35:01 And this is where it's tricky, because then… looks like there is some misalignment between the maintainers of the repo, that, okay, yeah, the PR looks good, I'll merge it, and the… requirement of having the component documented on another repo, which is not… part of my repo. For instance, I can give a real example. Like, in the demo, we got a couple of new components that are not reflected on the docs.
**tristan** 35:36 Hmm.
**Juliano Costa | Datadog** 35:37 like, I'm annoyed by that, but, like, I just have 24 hours on my day, and I can just do the things that I can do, like… Right.
I… but I… I… I know, and this bugs me, so, like, it, like, yeah, I know that I need to go and update this page, but… I think we should have better integration, or… I don't know.
**Perk (Marcin Stożek) | Elastic Ingest** 36:03 Is there… is there an emotion from the… from the communications SIG to… to make sure that other SIGs actually contribute to the documentation? Because I think that's a very fair ask, to ask the, you know, maintainers of this… of the thing to also take a look at the documentation. I think those two are… Not separate.
**Juliano Costa | Datadog** 36:27 So, I think that the problem here is… Keeping track of whatever is new.
For instance, on the demo, everything… every time there is an update on the docs.
Related to the demo, the docs guys ping the approvers from the demo, and we go and review.
The problem is that whenever we merge things on the demo that do not exist on the docs, so the docs is unaware of those changes, and if someone from the demo doesn't go there and create this page, update it, and document the new stuff.
That will never happen.
So, like, the discoverability of new things is just, bad.
And that, that, that is the same for basically all the other, SIGs, because… Things are new, and each language is… Moving in their own pace, but… Like, not necessarily the docs are following that.
**Perk (Marcin Stożek) | Elastic Ingest** 37:35 Sure, that's fair enough. It's, is there… do you know, maybe there is, I just don't know. Is there an… Intent for this to happen somewhere, like, codified? Because, you know, like, sometimes it helps if there are, like, rules that are not strictly, you know, in the CI that you shall not pass if you don't have it, but at the same time, if you have something written, then then people at least know that the direction is that, hey, if you change something, if you contribute something, then you should also take a look at the documentation. Is there anything like that? Like, a process or anything? Do you know?
**Juliano Costa | Datadog** 38:18 In the demo, we have a checkbox.
So when you open up your slide, like, updated docs.
**Perk (Marcin Stożek) | Elastic Ingest** 38:24 Hmm… Let me see.
**Juliano Costa | Datadog** 38:26 Is there a way to make that enforceable? I mean… Perk (Marcin Stożek) | Elastic Ingest 38:32 I'm not sure.
**Juliano Costa | Datadog** 38:33 Not at the same time? Go ahead.
**Perk (Marcin Stożek) | Elastic Ingest** 38:35 Yeah, I just wanted to say that I'm not sure whether that is enforceable, I think that is a very good call. Like, if you have a checkbook, like, how much more can you do? But then, I think at the same time, I always think it's, it's good… it's good to be, very open… very openly express your, your intent. Like, if the intent is for everybody to contribute to the docs, then it should be written somewhere, you know, publicly.
And then you can always, you know, like, point somebody to just say hi, but, you know, like, you gotta contribute to docs as well. Your work does not stop with the code. And that is true for, I think, every company in IT. So this should not be a surprise to anybody.
**Juliano Costa | Datadog** 39:19 I wonder if maybe we could… Create something… like a structured README, Or, I don't know, some sort of, markdown file that will leave On the… on the repos?
So each repo would have this Markdown file, or whatever, template file, Jinja, whatever. And this is responsibility of, each SIG.
But then, those files are consumed by the docs.
So, people do not need to actually go to the docs and update the docs, because when we have, like, two repos need… So, whenever a new PR comes in, you need to update here and there, and this and there, most of the times, do not work.
So, if we have something that… okay, so you are changing this component, you need to update this file. Great, okay, then I can have a GitHub action that validates if everything was, updated. Done, done, and then the docs will be, like, automatically updated. I think that.
**Perk (Marcin Stożek) | Elastic Ingest** 40:31 That would be…
**Juliano Costa | Datadog** 40:32 media, a cool… thing to discuss. I don't know how much that would work for… All the things that we have?
But, yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 40:43 I think that's interesting. I have a… I have a… I have Fabri here at Elastic locally. I'll just ping him and ask him what he thinks about that idea.
the… I see one little risk with that approach, although I like it. Like, you know, you have a project, like, let's say you have a collector, you have the SDK for PHP, like, you are responsible for the docs, and the docs lives inside your repository, so it's actually very clear, right? At the same time, I think the risk is that documentation should be coherent.
So I think it's easier to look at it if it lives in the same repository. Also, there are those, you know, translations and whatnot, and I think this one might be actually some… a little bit tricky, tricky to do.
**Juliano Costa | Datadog** 41:25 Yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 41:26 But the general… generally, yeah, it feels like, this could… this could be better. So, yeah, yeah, let me ping Fabri. Maybe I'll ask him to join, you know, next week.
**Juliano Costa | Datadog** 41:38 But another, another thing that I just, saw, like, I know that Weaver is new.
But we have been talking about Weaver for 2 years already, I think it was presented.
2 years ago at QCon. So… And there is no doc at all. There are blog posts about Weaver, but no… not a single page on… However, there is the repository, there are examples there, great, but, like, can't we have a doc page explaining how to use the use cases?
**Perk (Marcin Stożek) | Elastic Ingest** 42:14 That is interesting. Okay, I had no idea that the weaver dogs are not there at all.
**Juliano Costa | Datadog** 42:21 Yes.
So… But then, one thing that, is a downside of that, is that… would that be something that we would take care in the developer experience sake, or that should be something that should be… just… Best.
to the docs, to the comms, or to the SDKs, or should we raise to someone else, I don't know, GC level, so we can have a project?
Decision, top-down, and then every… everyone on the sub-projects would… have to follow this, whatever. Yeah.
I mean, yeah, it's… It's not easy, like, I don't know the answer, I'm just brainstorming here.
**Johanna Öjeling** 43:11 That's a good question, and I'm sure there are more areas also that… where documentation is missing, so it might be, like, a first step for us to identify where are the biggest gaps, like, where is documentation most needed, or yeah, and Weaver might be one of those, and yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 43:33 It actually feels… Peace.
**Johanna Öjeling** 43:35 Jonath, go ahead.
**Perk (Marcin Stożek) | Elastic Ingest** 43:37 I just know that it feels very natural for, for start looking at this from the lens of the developer experience, because this is the one when you look at things, you know, from the top, right? And then you see those gaps, right? So, I'm not surprised. To your point, Juliano.
Yeah, that's a good call. You never know who, how to approach such things, but you need a driver, and I think the driver coming from this SICK is a good call, you know? So it doesn't mean that we have to do it everything, but at least make everybody aware, and then we'll take it from there. We'll see.
**Juliano Costa | Datadog** 44:17 Yeah.
**Johanna Öjeling** 44:18 Could, coordinate and, like, nudge people and, you know, follow up and make sure, yeah, things.
**Perk (Marcin Stożek) | Elastic Ingest** 44:25 find an owner.
**Johanna Öjeling** 44:26 Yeah, exactly, yeah. Like, just, like, make sure it happens somewhat.
**Juliano Costa | Datadog** 44:33 when, when we bootstrapped the SIG, that was actually a point that Tristan raised. Like, if we identify an improvement on the SDK and stuff, we wouldn't be the responses for implementing, but we could, I don't know, create a mock-up, and then… present to spec, or present to the… to the SDK, to the.
SDK owners, and then have that, like.
being accepted, and then adopted, and then applied to all the sub-repos. So, it's not… it's not about, like, us driving the whole thing, but just, I think, yeah, agreeing with you here on, maybe identifying, proposing a solution, and then working with the rest of the community to actually… Define something.
**Perk (Marcin Stożek) | Elastic Ingest** 45:27 Yeah.
there are only so many battles that you can fight at the same time, right? But at least flagging, I think that's a very good thing to do here.
**Johanna Öjeling** 45:39 Yeah.
**Juliano Costa | Datadog** 45:40 Another.
**Johanna Öjeling** 45:40 Agreed.
**Juliano Costa | Datadog** 45:43 Sorry.
**Johanna Öjeling** 45:45 Yeah, I just… I agree. No, you go ahead.
**Juliano Costa | Datadog** 45:48 Another thing, Perk, I think Fabri has, access to stats on the docs.
So maybe we could use that to take more, directed action? Like, what are the pages that folks are more interested? What are folks asking AI, or what are the searches? And then maybe take a look at those and see where we can improve on that. I'm not sure.
Whoa.
**Perk (Marcin Stożek) | Elastic Ingest** 46:19 Yeah, I think it's a good idea.
So, you know what?
Maybe, maybe let me just ask him to join next week?
And, and, and we can have a conversation. What do you think? Cool.
**Juliano Costa | Datadog** 46:33 Yep.
**Johanna Öjeling** 46:34 That sounds great. And I know Tiffany in the communications thing, she has also run… like, when she's been working on re-architecting the collector documentation, she has run analysis and stack threads and so on to… to find out, like, what are the most Frequently asked questions, and yeah, where do people get stuck?
So that's also, like, a source of information we could use to see if we have Slack channels.
**Juliano Costa | Datadog** 47:02 Oh, nice.
I thought Tiffany was only on the right team.
**Johanna Öjeling** 47:11 Sorry, I'll be…
**Juliano Costa | Datadog** 47:13 on, on writing?
**Johanna Öjeling** 47:15 Yeah, exactly. She's, writing, but this was for, like, re-architecting the collector, pages on OpenTelemetry.io.
**Juliano Costa | Datadog** 47:28 Boop.
Nice.
**Johanna Öjeling** 47:31 Yeah, I don't know how far that project has come.
Actually.
Whether anything was changed after, yeah.
We'll check with her.
**Juliano Costa | Datadog** 47:52 the real hacker came in there, Brooke.
**Perk (Marcin Stożek) | Elastic Ingest** 47:55 Yes, yeah, yeah, there are other people here. Exactly.
You tell me, guys, whenever.
**Juliano Costa | Datadog** 48:03 That's enough.
**Perk (Marcin Stożek) | Elastic Ingest** 48:04 Because I don't.
**Juliano Costa | Datadog** 48:06 It is, yeah.
Okay.
**Johanna Öjeling** 48:23 Okay, but then we have a plan for next week.
**Perk (Marcin Stożek) | Elastic Ingest** 48:29 Yep. Excellent.
**Juliano Costa | Datadog** 48:31 Do we?
**Perk (Marcin Stożek) | Elastic Ingest** 48:34 Whoa.
Just several discussion, initial discussion, so that we can come up with a plan.
Afterwards.
But you gotta start somewhere, so… that's a good, good, good, good point.
**Juliano Costa | Datadog** 48:47 Okay. Then… Well, I think we can.
Wrap up for today.
**Perk (Marcin Stożek) | Elastic Ingest** 48:58 Awesome to see ya.
**Juliano Costa | Datadog** 48:59 appreciate it. Have a great rest of the week.
**Johanna Öjeling** 49:04 Thank you, you too.
**Perk (Marcin Stożek) | Elastic Ingest** 49:05 See ya around. Bye. Bye.
