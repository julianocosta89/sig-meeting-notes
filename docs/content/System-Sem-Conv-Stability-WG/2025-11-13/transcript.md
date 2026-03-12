SIG: System Sem Conv Stability WG
Date: 2025-11-13
Duration: 15 minutes
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 01:24 Hey.
**Braydon Kains (Google)** 01:26 Hello, how's it going?
**Pablo Baeyens** 01:29 Good, well… Did you figure out the changelog thing?
**Braydon Kains (Google)** 01:35 I'm pretty sure, because it's GitHub generated.
I have to add a metadata YAML file somewhere, or, like, the.
**Pablo Baeyens** 01:43 Could be, yeah.
**Braydon Kains (Google)** 01:45 Yeah, the GitHub Gen workflow fails when I try to manually add it.
**Pablo Baeyens** 02:04 I think this is going to be everybody today.
**Braydon Kains (Google)** 02:07 Yeah, I think so.
**Dmitrii Anoshin** 02:12 I have hooks.
**Pablo Baeyens** 02:15 Morning.
**Dmitrii Anoshin** 02:27 Braden, what do you just ask about metadata, Jen?
Can I help, or…
**Braydon Kains (Google)** 02:33 Maybe. It's not mdataGen, but it's actually, the… it's GitHub Gen.
**Dmitrii Anoshin** 02:40 Oh, okay.
**Braydon Kains (Google)** 02:41 I'm making a change to the ex-consumer error package, and I'm trying to Make the changelog, but the package isn't considered, like, a valid thing in the changelog gen config, and that's because it doesn't have a metadata YAML file, and so GitHub gen doesn't pick it up and put it in the config.
**Dmitrii Anoshin** 03:00 Yeah, but you can use whatever apparent of that package.
I guess.
**Braydon Kains (Google)** 03:06 Right, and… The parent doesn't have one either, so I can…
**Dmitrii Anoshin** 03:10 Okay.
**Braydon Kains (Google)** 03:11 I can add one to the parent. I wasn't sure if I should add one to the parent, or if I should add one, like, all the way down the line.
**Dmitrii Anoshin** 03:17 Which one that is X consumer error?
**Braydon Kains (Google)** 03:20 Yeah.
**Dmitrii Anoshin** 03:21 Probably, I would add both of them as a separate PR, and then you can replace them.
**Braydon Kains (Google)** 03:26 Okay.
**Dmitrii Anoshin** 03:27 Partial change.
**Pablo Baeyens** 03:49 If you don't have any topics, maybe we can check the board?
**Braydon Kains (Google)** 03:55 Yeah, I don't think I have any topics.
**Pablo Baeyens** 03:59 Okay… Give me a second and I'll share my screen.
**Braydon Kains (Google)** 04:06 Man, when you open the issues page, at least on my screen, every single issue that shows up is by the same person.
**Pablo Baeyens** 04:26 Yay, so, for process, we have these three… I think we mentioned something about asking you, Braden, last week.
**Braydon Kains (Google)** 04:44 Oh, yeah, this is… this is on my list. I… I keep on… procrastinating it, but I will do it.
**Pablo Baeyens** 04:57 Okay, on this one… we have the guidance. Okay.
**Braydon Kains (Google)** 05:04 Yeah, I think I think, actually, in the issue Christos opened, all three of the sub-issues are on me, so I will… I will catch up on those today.
**Pablo Baeyens** 05:15 No worries.
And this one was more… last week's decision made, and I think… We wanted to confirm that with you?
**Braydon Kains (Google)** 05:32 Yeah, and… I think I responded on the issue, but yeah, I… I think it's probably the right… right thing to do.
it feels a little silly to put the OS name in something like File Descriptor, but it genuinely is different if you're on Unix versus Windows, and there isn't really an easy way to… to communicate that through a name… through a metric name, rather than… rather than to put the OS. So, I'm okay with throwing the OS on it.
**Pablo Baeyens** 06:00 Right.
Okay, so we would go with.
**Braydon Kains (Google)** 06:02 With this.
**Pablo Baeyens** 06:03 basically.
**Braydon Kains (Google)** 06:04 Yep.
**Pablo Baeyens** 06:07 Okay, cool.
And then… This one…
**Braydon Kains (Google)** 06:21 Yeah, this is a more… I think a more general audit of, like, what requirement levels we've set on everything, and making sure it's actually what we wanted.
**Pablo Baeyens** 06:33 Yay.
So do we know what we want to do? Like, we know the required ones, but we don't know the… The odors?
**Braydon Kains (Google)** 06:46 Yeah, I think this is, This is kind of like an exercise for us to make that decision, to actually decide what we want.
**Pablo Baeyens** 06:58 Okay.
Does it… Makes sense to discuss it right now, or…
**Braydon Kains (Google)** 07:04 We could discuss it right now, or I could… I could comb through, and then, like, come back with a list of which ones I think, and we can… we can fight off the list, rather than… Then, just off the…
**Pablo Baeyens** 07:15 Up to you.
**Braydon Kains (Google)** 07:16 the YAML definitions. Maybe I'll do that, just so we have something as a baseline, and if people disagree with specific ones, we can talk it out that way.
**Pablo Baeyens** 07:25 Okay. Yep, that works for me.
Okay, I mean, that's… Seems like we're almost there for process.
**Braydon Kains (Google)** 07:36 Yeah, I think something we'll have to decide is that, james Thompson opened, like.
6 issues for system and process yesterday.
I'm gonna assume that we're gonna ignore those for stabilization.
**Pablo Baeyens** 07:57 I would assume that as well, but .
**Braydon Kains (Google)** 08:01 One of them… one of them he opened is something that exists, so I don't know… Why, he's… Oh, he's just getting all up in this… Whatever.
bleh.
**Pablo Baeyens** 08:23 So you're referring to D6, right?
**Braydon Kains (Google)** 08:26 Yeah.
**Pablo Baeyens** 08:28 Okay.
**Braydon Kains (Google)** 08:31 Yeah, I don't think any of them actually… our blocking stability.
**Pablo Baeyens** 08:47 Mmm… Yeah, it seems like a new thing.
**Braydon Kains (Google)** 08:51 Yeah, most of them are net new.
**Pablo Baeyens** 09:04 Also new.
**Dmitrii Anoshin** 09:22 This all can go after… after we stabilize, right?
**Braydon Kains (Google)** 09:26 Yeah, I think so.
**Pablo Baeyens** 09:27 So, you know…
**Braydon Kains (Google)** 09:28 Yeah, other than this one… I guess, needs to change, because… We changed where the OS name goes.
**Dmitrii Anoshin** 09:37 Hmm, okay. Do you know the officer, by the way? Where are they coming from?
With all the requests, I'm just curious.
**Braydon Kains (Google)** 09:44 Oh, it's just James Thompson being… Doing his usual thing.
**Dmitrii Anoshin** 09:50 So, you know James Thompson. I work with them, but I'm not sure I fully understand, like, which company was the focus of the work.
**Braydon Kains (Google)** 10:03 I… don't know.
**Dmitrii Anoshin** 10:05 Okay.
**Braydon Kains (Google)** 10:05 he… He comments on… every PR and opens most of the issues on the repo these days, and I'm not sure what the motivation is exactly.
**Dmitrii Anoshin** 10:18 I'm just curious. Yeah, if it's just helping with the stabilization, that would be great, but it doesn't seem like stabilization, because there are some specific requests here for additional stuff.
**Pablo Baeyens** 10:30 Yeah, some of them are… Maybe things that are on the… Implementation on, like… We'll have to take a look eventually, like, I don't know.
**Dmitrii Anoshin** 10:46 Okay.
**Pablo Baeyens** 10:52 It seems like he's referring to… This one, for example, which maybe doesn't exist on the… On the spec.
**Braydon Kains (Google)** 11:02 process disk operations? It might not, I don't remember.
**Dmitrii Anoshin** 11:05 Okay.
I see.
**Pablo Baeyens** 11:09 In any case, like, we can…
**Dmitrii Anoshin** 11:13 handled it.
That's great, if he's doing that, if he's just, like, defining whatever we have in the collector.
Like, partially, I guess, but that's fine.
We have, raw units here, all around the places.
**Braydon Kains (Google)** 11:32 All over the places.
**Pablo Baeyens** 11:35 Yeah.
Yeah, I mean, I think… If the default metrics are stable, the optional ones can be… Still… We don't need to mark those as stable, and .
**Braydon Kains (Google)** 11:50 It's fine.
**Dmitrii Anoshin** 11:52 Sounds good.
**Pablo Baeyens** 11:54 Okay.
Anything else?
That you want to talk about, Jay?
**Dmitrii Anoshin** 12:04 Because, do you folks… Whoa.
Are you going to plan to travel to Europe for Q1 EU?
**Pablo Baeyens** 12:17 Yes.
**Braydon Kains (Google)** 12:18 I've submitted talks, so I'm… if I get a talk accepted, then I'm… then my org will fund the trip.
**Dmitrii Anoshin** 12:23 Nice, nice. I, skipped this one, but I most likely will go to the Euro.
**Pablo Baeyens** 12:29 Yeah, it's… there as well.
**Braydon Kains (Google)** 12:31 Cool, we'll see you there and there.
I have a quick, more general collector question, actually, if we've got a minute.
**Pablo Baeyens** 12:40 True.
**Braydon Kains (Google)** 12:40 Does the exporter helper have anything like a dead letter Q?
**Dmitrii Anoshin** 12:46 What's that?
**Braydon Kains (Google)** 12:47 It's basically, like, if… for entries that fail to send because of, like, network connectivity, of, like, where… Like, sending those somewhere so that the logs aren't just dropped or lost.
**Dmitrii Anoshin** 13:01 Yeah, it's gonna be for a lower connector, I guess. We… We have that one somewhere semi-implemented, I would say, but no, there is nothing in the… In the export helper. Export helper, if it… there are retries, but once, like, something goes out of the queue, it never comes back until it either dropped or sent.
**Braydon Kains (Google)** 13:29 Okay.
**Dmitrii Anoshin** 13:30 So, you can… you can, configure… exporter helper to retry always, to always retry, right? And in that case, it will never leave the queue.
Until it's sent out.
But by default, I believe it's, like… 5 fridge rice, or something like that.
**Braydon Kains (Google)** 13:54 Okay, makes sense. I'm just trying to deal with, like, in our exporter, the… the Google Cloud client libraries have, like, retry logic of their own, so we don't leverage the retry logic in the sending queue.
Okay. But because of that, like, now when network goes out, the data's just kind of gone, and we have to figure out how to recommend people deal with that.
**Dmitrii Anoshin** 14:18 Why do we need another dry mechanism? I mean, you're an exporter?
**Braydon Kains (Google)** 14:24 I don't know if there's a way for us to turn it off in the client libraries is the problem. So, like, the client libraries are gonna do retries.
And… I don't remember if the exporter helper… if you can just, like, turn it on in the exporter helper, or if we, like, force it off.
Maybe the forcing it off thing is the wrong idea.
I only just… I just got the issue this morning, so…
**Dmitrii Anoshin** 14:48 Okay.
The client that sends data to the collector, even.
**Braydon Kains (Google)** 14:52 No, the client that we… the library that we use to send data to Google Cloud from the exporter.
**Dmitrii Anoshin** 14:59 Oh, I see what you meant.
**Braydon Kains (Google)** 15:01 It does its own retry pooling.
**Dmitrii Anoshin** 15:03 Oh, okay, okay, okay, I see.
Yeah, but you can potentially just get rid of the client, I guess. It's still, like, some… underneath is some…
**Braydon Kains (Google)** 15:13 It's…
**Dmitrii Anoshin** 15:14 Your PC, right?
**Braydon Kains (Google)** 15:15 Yeah, it is… it's… it's some gRPC retrying pool. I don't know how it works yet.
**Dmitrii Anoshin** 15:27 Okay.
**Braydon Kains (Google)** 15:29 Alright, thank you.
**Dmitrii Anoshin** 15:31 Thanks, folks.
**Braydon Kains (Google)** 15:32 Talk to you later.
**Pablo Baeyens** 15:32 Alright, back to you.
