SIG: Developer Experience SIG Meeting
Date: 2026-02-11
Duration: 44 minutes
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 01:14 Hello, hello.
**Johanna Öjeling** 01:15 Hey, morning! How are you doing?
**Juliano Costa | Datadog** 01:19 All good. Yourself?
**Johanna Öjeling** 01:22 Doing well.
**Juliano Costa | Datadog** 01:24 Just kicking out Read AI, yeah.
**Johanna Öjeling** 01:27 Yeah, just so… We got it, yes.
**Juliano Costa | Datadog** 01:33 Nice work on the… on the blog post, thank you, yeah.
**Johanna Öjeling** 01:38 Oh, thank you!
Yeah, it's, I'm… yeah, I quite enjoy writing, and, it was nice to have the interview recordings, It's, I… I mean, my… my job is a software engineer, but I like to, like, engage in developer advocacy kind of work as well, so it's nice to, yeah, be involved here in the DevEx. Awesome.
And you're a developer advocate?
**Juliano Costa | Datadog** 02:12 Yeah, back… Two years ago, I was a software engineer.
**Johanna Öjeling** 02:18 Okay!
**Juliano Costa | Datadog** 02:19 What?
**Johanna Öjeling** 02:20 What made you, change?
**Juliano Costa | Datadog** 02:23 Mainly the… sorry.
My eyes… My eye is just, like, yeah, not working.
basically was the community work, actually. I was already doing some… some stuff in the hotel space, and also I run a meetup here in Leeds, in Austria.
**Johanna Öjeling** 02:48 -
**Juliano Costa | Datadog** 02:49 And then I had a… I got a kid, and I was like, okay, yeah, I need to do those things as work, so then…
**Johanna Öjeling** 02:56 Thank you.
**Juliano Costa | Datadog** 02:57 I enjoy my time off work with him.
So, yeah, and then at the same time, I got the… we got this position at Datadog that I would be focused on OpenTelemetry, and I said, okay, yeah, this sounds like, A good fit, so…
**Johanna Öjeling** 03:17 That's how…
**Juliano Costa | Datadog** 03:18 I ended up here.
**Johanna Öjeling** 03:20 Nice! And do you have… some kind of, kind of, activity that you enjoy more, like.
Yeah, like you mentioned, meetups, organizing, and, like, speaking, or… or do you enjoy, kind of, doing a bit of everything?
**Juliano Costa | Datadog** 03:38 I think it… Speaking is fun, but I, I like to build these stories, so I had a lot of fun, on my previous talk, called Smells Like Clean Telemetry, where… It was all based on Nirvana songs and, like, really, fun to build and create the content shaped in that In that form, in that format.
But I think what I like most is everything that happens Before and after the talk itself.
Other discussions that we have in the community.
**Johanna Öjeling** 04:22 -
**Juliano Costa | Datadog** 04:22 those discussions are the most valid ones. Like, going on stage and presenting is, fun, because you build the story and you wanna… you wanna share.
But I think connecting and discussing the things, like.
Even things that, you may be doing wrong, or things to improve, and… Ideas to the… to the community as a whole, is what I enjoy most.
**Johanna Öjeling** 04:50 - oh, yeah, I can completely relate to that. I, I started public speaking quite recently, and I'd never considered it before, but I thought, okay, I'll give it a try, and then I realized, like, wow, it's… Like, yeah, delivering the talk, it's, like, one thing, but what really, is rewarding is connecting with people afterwards, and people will, yeah, come to you and ask questions, so it's, like, a great opportunity to connect with people and, yeah.
**Juliano Costa | Datadog** 05:24 Yeah, totally.
Yeah, I… yeah, 100%. Where are you based, Johanna?
**Johanna Öjeling** 05:32 In Sweden, in Maldives, southern Sweden.
**Juliano Costa | Datadog** 05:35 Okay, Is that far from… so I… I'm asking because I'm… I run a meetup here in Lean's, and we are always looking for speakers, so if you want to try it out, a talk that you… build. We have a small community, which I think is ideal for those type of, tests.
**Johanna Öjeling** 05:58 -
**Juliano Costa | Datadog** 05:59 Yes.
I think the feedback that you get in smaller communities is better than, like, at KubeCon, where you have 1,000 people.
They need to go to other talks, and they never meet you again.
**Johanna Öjeling** 06:12 Yeah, -
**Juliano Costa | Datadog** 06:14 But in small communities, you present, and then you have, like, this networking, where people are eating snacks and drinking, and that's, like, where you actually connect.
**Johanna Öjeling** 06:24 - that's true. Nice, so…
**Juliano Costa | Datadog** 06:28 a monthly event.
**Johanna Öjeling** 06:28 Hardlings, or how do you.
**Juliano Costa | Datadog** 06:31 Yeah, L-I-N-Z.
We have monthly events, and we are always looking for speakers, so…
**Johanna Öjeling** 06:40 Huh.
**Juliano Costa | Datadog** 06:40 You plan to travel around, I don't know, you were at, Grafana, right?
**Johanna Öjeling** 06:47 Yes, exactly.
**Juliano Costa | Datadog** 06:48 I think you're gonna have an off-site in… Indiana.
**Johanna Öjeling** 06:53 Yeah, I was just thinking about it, like, yeah, sometime in August, yeah, then I'm going to Vienna.
**Juliano Costa | Datadog** 07:00 Yeah, that's… I told Marilia that this is actually unfortunate, because in August, we skipped the meetup, because it's summer, so everyone is on the holidays, and…
**Johanna Öjeling** 07:13 Clear.
**Juliano Costa | Datadog** 07:13 do not, dual event, but I… I think if we get, like, it's, like, once in a life… not a once in a lifetime, because Europe is small, and of course, you can, travel, there will be other chances, but, if it is something that is, like, really a unique opportunity, maybe we… I can discuss with the co-organizers, and we can, spin up something, and… A train from Vienna to Leinz is, like, 1 hour, 45 minutes, 2 hours.
**Johanna Öjeling** 07:51 Okay, - Cool, yeah.
**Juliano Costa | Datadog** 07:55 -Oh, I…
**Johanna Öjeling** 07:57 Stay in touch about this and see if… yeah.
**Juliano Costa | Datadog** 08:01 Okay, we have a meetup in 2 weeks, and I'll… I'll bring the topic up to them, and discuss. Maybe even discuss with the community itself, like, the folks that are attending, because we do the events for them, and, if… they do not want to join August, then it wouldn't make sense, but if they say, yeah, no, August is fine, then let's do it.
**Johanna Öjeling** 08:25 -
**Juliano Costa | Datadog** 08:27 Yeah, that would be cool, yeah.
**Johanna Öjeling** 08:29 Yeah, - yeah, it will be my first… no.
No, I've been to Austria before, actually, but yeah, it will be my first time in Vienna, that area.
Nice.
**Juliano Costa | Datadog** 08:40 Cool.
**Johanna Öjeling** 08:41 What is, Lynn's like?
Enter…
**Juliano Costa | Datadog** 08:45 Yeah, it's a… .
**Johanna Öjeling** 08:47 Right, it's that I hadn't… I don't think I've had a dog before, so…
**Juliano Costa | Datadog** 08:51 Yeah, me neither. I moved to Leanz because I was hired by Dynatrace, and their engineering headquarters is here.
**Johanna Öjeling** 09:02 Okay!
**Juliano Costa | Datadog** 09:03 So we moved here… my wife and I, we moved here, and then, like, after a couple of years, I migrated to Deratoc, but, now we have a kid, and, like, yeah, we like the city, so we are staying.
**Johanna Öjeling** 09:15 -
**Juliano Costa | Datadog** 09:16 In Austria itself, I think we are 3 employees in Austria.
**Johanna Öjeling** 09:23 Right.
**Juliano Costa | Datadog** 09:23 I'm in Datadog, so we don't have an office, or even a co-work, or whatever, so… I met the… funny enough, I've been in Datadog for 2 years, and I just met the other guy, one other guy from Austria two months ago, so… Yep.
**Johanna Öjeling** 09:43 Oh, because he, the other two are based in Vienna, and I'm based in Lynx, so yeah, we don't… Okay, okay.
**Juliano Costa | Datadog** 09:49 And they are from different teams, so, yeah.
**Johanna Öjeling** 09:53 Oh, okay, yeah. Hmm.
**Juliano Costa | Datadog** 09:55 So Leeds is… about 280, 260,000 people. It's a small city. Well, it's big for Austria, but, like, if you compare it to Brazil, where I'm from is small.
**Johanna Öjeling** 10:12 Mmm.
**Juliano Costa | Datadog** 10:12 And, like, I think we have good public transport and all this stuff that you look when you are… you look for when you're, building a family, so then we… We just like here. I don't like too much Vienna, because it's busy, and people are always in rush, and like, yeah, they're not the friendliest… the friendliest.
**Johanna Öjeling** 10:35 person in the world, but… Okay.
Yeah, it sounds really nice. And it's impressive that you have an observability community.
**Juliano Costa | Datadog** 10:48 Well, we run a cloud-native, meeting.
**Johanna Öjeling** 10:52 Oh, okay, -
**Juliano Costa | Datadog** 10:54 But we discuss a lot of topics.
about the cloud native space, there are a lot of observability topics, because, again, Dynatrace engineering headquarters here, and we often get, some speakers from them.
And I'm also in the, hotel space, so every time I can, I bring someone, and every time I hear, whatever. Like, last year we had… Rhys Lee from New Relic, and Adriana from Dynatrace, they were in Vienna for the Open Source Summit.
So then we invited them to join, but Austria got, like, a week of rain, and all the… all the railways were closed, and it was a mess, so they couldn't come, so they did a virtual… we did a virtual meetup with them in Vienna, and we… which was like, come on.
That's it. Usually, we have two talks on the night, and yeah, the community is super friendly. I enjoy doing this, so that's why I actually decided to… To migrate to developer advocacy.
**Johanna Öjeling** 12:13 Mmm, - Cool. And you're also involved in the… or you're a maintainer of the hotel demo, right, you mentioned? Yeah. Last week, I think, yeah.
**Juliano Costa | Datadog** 12:24 Yeah, that's how I started in the hotel space.
**Johanna Öjeling** 12:28 Okay,
**Juliano Costa | Datadog** 12:30 I've been involved in the demo since the beginning.
So, that was actually how I started with OTEL.
**Johanna Öjeling** 12:40 school.
**Juliano Costa | Datadog** 12:41 This is a Kustari, yeah, sorry if I'm oversharing.
**Johanna Öjeling** 12:46 No, no, not at all, it's interesting to hear.
**Juliano Costa | Datadog** 12:49 I… I was building a demo, so, like.
When hotel started to get some traction.
the other tracer wanted to test, like, how would, hotel data work with their agent? So, like, if the traces would be connected, if the context propagation would work, and everything. So I started building, kind of, Some services to put in between, or in front of.
Services that were instrumented with, diameteries.
And for that, we were using the hipster shot from Google. I don't know if you have ever seen.
They have a… it's called Microservices Demo that is maintained by Google for ages.
**Johanna Öjeling** 13:37 Okay,
**Juliano Costa | Datadog** 13:38 And, they have, like, I think it's about, 10 microservices?
And they use 5 different programming languages. Go, Python.NET, Java… And… Whatever.
I think, JavaScript.
And then I… I was doing this, at work, and I said, okay, yeah, you know, I need to learn better, hotel, so what if I get this demo?
rip… rip off everything that is Google-related, because they had, OpenSense was on it, and a bunch of, other stuff that wasn't related to… and some… some Google stuff unrelated to Otel. So I cleaned up everything, and deployed Hotel in All Services, and, Jaeger.
I published this, and then a colleague from Dynatrace, Army, that is involved in the technical committee and involved in the community, he said, hey, Carter from Microsoft started the discussion to create a hotel Demo.
Because he saw that.
all vendors were creating their own demo to showcase hotel, so it would make sense to have an upstream hotel demo vendor agnostic that all the vendors could rely on, because then we can reuse that work, and we work together as a community, and then everyone can take advantage of it.
I said, well, this is a cool idea. So I joined the pre-Seek meeting.
And we agreed to do a research on all the… all the forks from this hipster shop that existed.
to kind of start the project of the OpenTelemetry demo based on this.
And from.
all the samples that were available, open source, mine was the only one that didn't have any vendor-specific stuff. Honeycomb had their demo, even Diamondrace had their own demo, and other vendors had their Hipster Shop demo.
But, of course, all of them added some vendor-specific stuff to the demo.
**Johanna Öjeling** 16:00 -
**Juliano Costa | Datadog** 16:01 And mine was just for a study, so I just had hotel and Jaeger. So then my fork was the initial co-donation for the demo.
**Johanna Öjeling** 16:11 Yay!
**Juliano Costa | Datadog** 16:13 Then we invited all the contributors from… all the maintainers from the other… programming languages to actually rewrite some microservices in their own language. So that's how today we ended up, we ended up with, I think 17?
**Johanna Öjeling** 16:32 Who's hers.
**Juliano Costa | Datadog** 16:33 One of each, one of each… each one of them written in a different programming language, which is a mess, but it's awesome to showcase, like, how each language works, and the flow of the data and everything.
**Johanna Öjeling** 16:50 Yeah, it's a really, comprehensive, project, and I think it's super useful. I use it all the time when I need to demo something about, like, the OCAP Collector, or, like, yeah.
Let's…
**Juliano Costa | Datadog** 17:05 Yeah, I use it all the time as well, and I enjoy it.
And one thing that I really enjoy is walking, at the KubeCon booths, and all the vendors are using the demo.
**Johanna Öjeling** 17:20 I see the…
**Juliano Costa | Datadog** 17:21 services names, and it's how, yeah, I know… I know these trees.
Yeah, it's so pretty cool.
**Johanna Öjeling** 17:28 April, yeah.
So, what… what does the work involve today on the demo? Are you… Like, expanding it, or is it mostly about maintaining what's in there, or… What does your, kind of, involvement look like, do you think?
**Juliano Costa | Datadog** 17:46 So… Currently, my struggle is finding contributors.
bring other stuff to the demo. But, the… we have some… some stuff in motion, like, keeping… just keeping up to date with the hotel collector changes.
We are in our work for… to… to the… in a road to the stabilization in 1.0, so that has a bunch of changes that… for instance, recently, the… OTLP was renamed to OTLP underscore JRPC, because we already had the OTLP underscore HTP, so, like, things that break, and then… This, will also break.
all the vendors' integrations, so yeah.
**Johanna Öjeling** 18:34 Okay.
**Juliano Costa | Datadog** 18:36 properly communicate. But, like, a couple of months back, we had a service that is a mock-up of OpenAI call.
**Johanna Öjeling** 18:45 Excuse me, man.
**Juliano Costa | Datadog** 18:46 have a service… an uninstrumented service LLM that returns some answers.
from 3 specific questions, and of course, the traces that are produced from the service that is calling this service are, like, following the GenAI semantic conventions.
you can also replace the mock-up service with your LLM, or with your OpenAI API key, and then it would actually call OpenAI.
**Johanna Öjeling** 19:19 So, there's.
**Juliano Costa | Datadog** 19:19 This is cool. Now we got, a PR from Martin Twitz, from Honeycomb, to add Weaver to the demo as well.
**Johanna Öjeling** 19:31 We try.
**Juliano Costa | Datadog** 19:32 I try to kind of… it's hard to keep keep it, like, under control and not, overdoing stuff, but yeah, I think.
**Johanna Öjeling** 19:42 -
**Juliano Costa | Datadog** 19:42 we… we are way past the overdoing stuff, so it's already, like, a monster. And this was one of the discussions that we had at the Hotel Unplugged.
**Johanna Öjeling** 19:55 People would like to have.
**Juliano Costa | Datadog** 19:59 Smaller demo to run.
And, like, be able to spin up, like, locally, without.
Destroying their computers.
**Johanna Öjeling** 20:11 Oh, okay.
That's true.
**Juliano Costa | Datadog** 20:15 Yeah.
This is, what I've been doing.
**Johanna Öjeling** 20:19 Yeah, wow, interesting to hear the, yeah, story out there.
**Juliano Costa | Datadog** 20:26 Cool. Tristan.
**tristan** 20:27 Interesting.
**Juliano Costa | Datadog** 20:27 system.
**tristan** 20:28 Sorry, I'm late.
**Johanna Öjeling** 20:30 Rice.
**Juliano Costa | Datadog** 20:33 We were… we were chatting about life. Hold on.
**tristan** 20:36 Yeah.
**Juliano Costa | Datadog** 20:40 But now that you are here, I want to bring up one thing, also to discuss that with Johanna.
Yeah. So, Johanna, I don't know if you saw, but if you navigate to the Dansk, Post that Tristan wrote.
He has a couple of drawings that I converted to… to, like, a… An image, or, like, an illustration, whatever.
**tristan** 21:17 Joe?
**Juliano Costa | Datadog** 21:18 I think we should… I think we… we need to… To agree on, pattern, so to say. I saw that you created a nice one for Adobe.
Yeah.
**Johanna Öjeling** 21:35 Yeah, exactly, it was, Bogdan showed some slides in the presentation, but then also… but yeah, I agree, it would be great to… To kind of use the same tooling, and format.
**Juliano Costa | Datadog** 21:53 Yeah, I enjoyed the RS, very much. Where did you… Where'd you do… Try it.
**Johanna Öjeling** 22:01 I used, Excalibro.
**Juliano Costa | Datadog** 22:05 Okay, so it's the same… It's the same as.
**Johanna Öjeling** 22:07 Do you… Yeah, but okay, it looks like, yeah, just we use different… edges, so, yeah, I can… I mean, I can redo it, it's quickly.
**Juliano Costa | Datadog** 22:20 I can also change mine as well, so we just need to agree on,
**Johanna Öjeling** 22:25 Yeah.
**Juliano Costa | Datadog** 22:26 whatever we do. I also use the collector logo that is not well known.
**Johanna Öjeling** 22:32 Oh,
**Juliano Costa | Datadog** 22:35 But it is, like, it is in their… in their REPL, so… I don't know if… Let me.
**Johanna Öjeling** 22:43 Let me get… Logo.
**Juliano Costa | Datadog** 22:45 One sec.
I think in the… Open telemetry… Red Pull… Or is it in the GitHub?
One sec, I'll share in a sec.
But I think we are in a… in a good shape, actually.
Tim told me that he would Do the final review and approve or not, yesterday.
from the Mastodon one, and he didn't, so I was… I had hopes.
He replied to me, he said, hey, I will take a look later today.
But yeah, I think the Macedon one is ready to go, and the Skyscanner is also… I mean, now with, Tristan's comments, we may need to… Add some snippets.
**tristan** 23:47 Yeah, depending on what you think of that, and if they'll… if they'll supply snippets. Like, I was just thinking the… I'm trying to get it from Doncs, too, that they have, like, wrappers and niceties, and it would just be… Cause it's one thing to… Like, people reading this, they'll be like, they'll see it, and they'll be like, oh, they use rappers. It's like, but what is that?
really mean in practice, so being able to show something might… might… I don't know, I feel like it… Adds a lot to it.
It's really…
**Johanna Öjeling** 24:22 I think that's, yeah, a great idea. Thank you for, reviewing it. I'll, yeah, I'll check with Neil again if, yeah, if there are any snippets he'd like to share in those sections, or, yeah, and it's nice, yeah, as a reader to… also, that there's just not a big, you know, chunk of text, but yeah.
**tristan** 24:41 And same with, like, parts of the… the… the, collector config. Like, it can be nice, like, the… I think I mentioned the filter processor for the 404s, and… There might be some other things just to, you know, give people examples of how they would use it, versus just saying in words how it is used, yeah.
**Johanna Öjeling** 25:06 - Yep, true.
And, Neil was also waiting for… Yeah, he would run it through their PR and communications department, too. Yeah.
see that the facts in the intro are correct. Yeah, I think then, once adding, config snippets, potentially some diagram, and getting their approval, that one will be also… Good to go.
Oh, thanks, Adriana.
**Juliano Costa | Datadog** 25:39 Yeah, I shared here, there is, under the OpenTeLentry I.O, a folder called Econography.
Iconography? I don't know how to pronounce that. But there is the collector PNG.
**Johanna Öjeling** 25:55 Oh, nice.
**Juliano Costa | Datadog** 26:03 We even have a OTLP logo. Oh, nice. Never, never saw that before.
Today I learned.
And we have an open underscore telemetry.
I am not happy about seeing the underscore here.
**tristan** 26:32 It's 5 years old, that's why.
**Juliano Costa | Datadog** 26:35 Okay.
**tristan** 26:38 A lot of these are… I wonder… they must have just copied these from somewhere?
**Juliano Costa | Datadog** 26:43 Hmm.
I don't… I know that I contributed the converters and extensions.
So I added those two icons there.
**tristan** 26:57 It is.
**Juliano Costa | Datadog** 26:59 Because I was reviewing a presentation from a colleague, and he had, like, a list of components, like, all text, and I said, oh, this is ugly.
So then I said, okay, let's add the icons. And then we had, like, receivers, processors, exporters, icons, but we didn't have, like, connectors.
**tristan** 27:21 Hmm.
**Juliano Costa | Datadog** 27:21 and, extensions, so I said, wow.
It's a good opportunity to.
to add one. So, yep.
**Johanna Öjeling** 27:39 That's how I found out about the collector logo.
Cool.
Yeah, I'll paste that also into my image. But then, should we go with, rounded edges, or what should we… any preference?
**Juliano Costa | Datadog** 28:01 Tristan?
**tristan** 28:02 I think rounded looks nicer for some reason, I have no idea why, but…
**Johanna Öjeling** 28:07 Yep.
Right, then I'll, update the… Adobe Image.
**tristan** 28:15 Cool.
**Juliano Costa | Datadog** 28:17 Cool.
Adobe… Okay, so, and you also add… added app to the… to the… container itself.
**Johanna Öjeling** 28:30 Oh.
**Juliano Costa | Datadog** 28:31 And.
**Johanna Öjeling** 28:32 Bye.
**Juliano Costa | Datadog** 28:33 Don't.
I just have, like, container. We are also using different phones.
But I think yours is better.
So, I will change mine to use… The… what is the font name, do you know?
**Johanna Öjeling** 28:53 Hmm… let's see… I just used the default one.
Let's see… Awesome.
I didn't even know I could configure the phone.
Oh, fault family, okay.
Aha!
**Juliano Costa | Datadog** 29:16 But maybe, maybe yours is actually easier to read.
**Johanna Öjeling** 29:20 Oh, sure.
**Juliano Costa | Datadog** 29:21 Let me… let me share my screen real quick here.
**Johanna Öjeling** 29:27 Okay, so mine is called Excalifont.
**Juliano Costa | Datadog** 29:32 Okay, so is it… what? I actually don't know where to configure the font.
**Johanna Öjeling** 29:38 No, I didn't know either, but yeah.
**Juliano Costa | Datadog** 29:40 Yeah, excellent.
**Johanna Öjeling** 29:41 button.
**Juliano Costa | Datadog** 29:41 Okay.
**Johanna Öjeling** 29:42 Yeah.
**Juliano Costa | Datadog** 29:45 I don't know which one is more, readable.
I mean, for accessibility…
**Johanna Öjeling** 29:57 Yeah, I think, actually, this one is… Better.
**Juliano Costa | Datadog** 30:04 Okay.
**Johanna Öjeling** 30:06 Mmm… This one is called Nonito, right?
**Juliano Costa | Datadog** 30:13 Here you added… oops.
It's tough moving.
This one, cute question. I think if you click the font, you can select the middle one.
**Johanna Öjeling** 30:27 Yeah, that one, yeah.
**Juliano Costa | Datadog** 30:29 Let me see the name…
**Johanna Öjeling** 30:31 Yeah, no need to. Okay, yeah, no need to.
**Juliano Costa | Datadog** 30:38 How do I add a text?
It was just…
**Johanna Öjeling** 30:52 This fault.
Okay.
**Juliano Costa | Datadog** 30:57 So, I will… add up here.
**Johanna Öjeling** 31:03 If you click one of your boxes, Just want to see how… If we use the same settings. Okay, yeah, it looks the same, the stroke width, the stroke, yeah, stop enough, but yeah, good.
**Juliano Costa | Datadog** 31:21 Okay.
Mido and middle. Perfect.
Okie dokie.
So…
**Johanna Öjeling** 31:31 Then maybe we get the first, blog post published soon.
**Juliano Costa | Datadog** 31:37 Yeah, let's see if one of them can come back.
Tristan, do you have any… Anyone from… Dansk that we can invite to the…
**tristan** 31:54 Oh, right, invite to the deck.
**Juliano Costa | Datadog** 31:55 Yeah, so I will… I will add the review tracker on the top of the…
**tristan** 32:01 Yep.
**Juliano Costa | Datadog** 32:03 dusk.
**tristan** 32:04 Yeah, I'll add somebody.
**Juliano Costa | Datadog** 32:07 Of course, I will clean up.
**tristan** 32:08 I'm trying to get them to get back to me.
**Juliano Costa | Datadog** 32:13 Team. No… Hold on.
And… To add myself.
And… someone else.
Cool.
Okie dokie.
Anything else that we need to… To discuss?
I do, I do have another thing. So, Tristan, if you go to Skyscanner post.
So, johanna, what she did, or the choice that, she… she made, and I think it's, interesting one.
She added the whole hotel being as a link.
**tristan** 33:50 Right.
**Juliano Costa | Datadog** 33:51 So, when we mentioned the Gateway Hotel Bean in… in the text.
**tristan** 33:59 People can actually navigate to HotelBin and see, zoom in, zoom out.
**Juliano Costa | Datadog** 34:05 Do all that stuff.
I think this is a nice approach, because this is actually something that I mentioned on the Mastodon blog.
that I got the image from HotelBin directly, and it would be awesome to have a better resolution.
And the more wide it is, the smaller it is, so I don't think it's actually valuable to whoever is.
**tristan** 34:32 Yeah, they get too big.
**Juliano Costa | Datadog** 34:33 utilizing.
Yeah, and in the hotel I.O. page, I don't think we have the functionality to zoom in images. So, like, if you click the image, it expands, or something like that. I don't know if they added it.
**tristan** 34:50 over it.
**Juliano Costa | Datadog** 34:51 But that was a complaint that I got on the, on the demo screenshots.
**tristan** 34:58 That's why I know.
**Juliano Costa | Datadog** 35:03 Yeah, so.
**Johanna Öjeling** 35:05 Yeah, I think it's nice also, like, if… if the company's willing to provide their config, and yeah.
publish it on, Ottin. It's, it's easier… also, like, if it's a very large config, it would be difficult to have it in the blog post, like, it would take up, like, yeah, so many pages. So I think, yeah, having, like, some select snippets in the blog post, and then, yeah, having a link to where they can read the entire config and, yeah, zoom in and out.
**tristan** 35:38 And even if the… With the snippet, if the image, like, that portion of the image is useful.
To, like, visualizing the snippet? Like, just cutting it down to that little section?
**Johanna Öjeling** 35:54 Hmm.
**tristan** 35:55 And including that would be nice.
Might not be very useful, but the… Like, yeah, there could be cases where, like, showing… I don't know, routing going off into 3 other blocks, and just cutting it down to those, yeah.
**Johanna Öjeling** 36:21 Great to get context on, like, where this specific configuration fits in.
**tristan** 36:26 Yeah, but then, yeah. Overall, just having a link to the hotel bin and not trying to force in that image makes sense… makes sense to me.
**Juliano Costa | Datadog** 36:37 Oh, so… Just to align here, then, with… Johan and Tristan, if you navigate to the Mastodon draft, you would drop the config from here, on the… right after the hotel being screenshot.
**Johanna Öjeling** 36:56 Oh…
**tristan** 36:58 Hmm…
**Johanna Öjeling** 37:01 Yeah, I think it would be.
**Juliano Costa | Datadog** 37:07 Yeah, I can add the link to Autobin.
**Johanna Öjeling** 37:10 Oh, yeah, this is, in the, from the hotel operator, but yeah, if we can…
**Juliano Costa | Datadog** 37:20 true. Yeah, this is a different approach.
**Johanna Öjeling** 37:22 The… from the config… section. We could copy that, too. It would have been, maybe, and…
**tristan** 37:33 Yeah.
I mean, theirs isn't too bad compared to the other ones, but… So, it could go…
**Johanna Öjeling** 37:39 Oh, yeah.
**tristan** 37:42 I mean, you could still include it and also have the link, so I'm really… yeah, I could go either way on theirs.
The other ones were so big, they wouldn't, yeah.
**Johanna Öjeling** 37:52 Yes.
**Juliano Costa | Datadog** 37:55 And also, I think Skyscanner has a couple of different ones, right?
**Johanna Öjeling** 38:00 Exactly, yeah.
**Juliano Costa | Datadog** 38:11 Okay.
Okay, okay.
**Johanna Öjeling** 38:17 Or maybe… I mean, if they're, on… on the blog post on Optometry.io, if If it's possible to, like, expand and collapse the config, you know.
**Juliano Costa | Datadog** 38:33 That's a good, a good point. I don't know.
Let me click around.
I don't think we have, this… Functionality, or… this, thing used anywhere?
but maybe…
**Johanna Öjeling** 39:28 Cute.
**Juliano Costa | Datadog** 39:32 C… I mean, it would make sense to have these semantic conventions, but no, we also don't have… You have a bunch of, subpages.
And… Just go from one to the other.
**Johanna Öjeling** 39:53 Oh, okay.
**Juliano Costa | Datadog** 40:03 But I can check that, so I'll add a note to myself, Boop.
**Johanna Öjeling** 41:01 Great, and for the Adobe one, Bogdan saw my message in the Slack yesterday, so he came back with his email address on the show.
This morning, so yeah. I'll take a look.
won't you? And, they didn't share any configs that I'm aware of, but I asked if Yeah, there wasn't anything. They seem to be quite secretive about, like, which vendor they use, and yeah, some details, so let's see what's… what's possible to share for them.
**tristan** 41:39 They might as…
**Juliano Costa | Datadog** 41:39 even… even if we can get, like, all the things that they use and replace the vendor with Hotel P, and just call, like, Hotel P slash vendor, I think that would be nice. I know that there are some companies that are not public.
**Johanna Öjeling** 41:57 Users.
**Juliano Costa | Datadog** 41:58 Chrome… From the vendors.
**Johanna Öjeling** 42:00 Exactly, so…
**Juliano Costa | Datadog** 42:02 Sometimes they do have nice stories that I wanted to share, but yeah, I can't.
**Johanna Öjeling** 42:06 Yeah, exactly. No, but I think, because me, like, he had edited all of his config, too, and just wrote, like.
vendor.com, like, yeah, marine Dadra song.
Cool. Yeah.
**Juliano Costa | Datadog** 42:27 Yeah, I think for the goal of what we are trying to achieve here, having… having… Vendor is enough.
Like, or Utopia, or whatever. Unless they have… some… some pain points with the collector configuration because of, the way that the vendor works, as Mastodon shared, like…
**Johanna Öjeling** 43:04 Oh, baby.
**Juliano Costa | Datadog** 43:05 I had to do some transform on the spend names to actually add a new type of, attribute called resource that we have in Datadoc, so this was something that, it was, like, at the beginning, a bit difficult and a bump to them to configure, and yeah, I think it's valid to add to the story.
But other than that, if it's just an endpoint that they send the data, then… Doesn't… it doesn't add anything to the… to this room.
**Johanna Öjeling** 43:42 Yeah.
It's true.
**Juliano Costa | Datadog** 43:49 Okay.
**Johanna Öjeling** 44:02 Rick, anything else?
**tristan** 44:06 Guess not.
MCP's waiting on a TC decision, but that's about it.
So…
**Johanna Öjeling** 44:18 Yeah, hopefully it can be much sooner.
**tristan** 44:24 Probably.
Alright.
We can call it here, then.
**Juliano Costa | Datadog** 44:29 Thanks. Capro?
**Johanna Öjeling** 44:32 See you. Have a good day.
**Juliano Costa | Datadog** 44:33 Copy.
