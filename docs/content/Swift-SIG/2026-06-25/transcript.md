SIG: Swift SIG
Date: 2026-06-25
Duration: 18 minutes
============================================================

## Zoom Recording Transcript

**Ben Joseph** 02:15 Hi, Ted.
**Ted Young** 02:20 Hello?
How you doing?
**Ben Joseph** 02:23 I'm good, how are you?
**Ted Young** 02:24 Doing good!
That's twisted, and say hi.
**Ben Joseph** 02:29 Yes, I believe we've not met. I recently joined Grafana in the mobile OLE team.
**Ted Young** 02:36 Yeah, yeah.
**Ben Joseph** 02:37 Yeah, I…
**Ted Young** 02:38 Nice.
**Ben Joseph** 02:39 Yeah, I've been meeting with other folks, like Martin, on the client side. So, yeah, I do not have much iOS experience, but I'm hoping, like, anyway, I'll be working on the iOS side of things at Grafana, so I thought, like, I'll start joining the SICK meetings to at least see the direction of how things are heading.
Yeah, I, I just… this is my second, meeting,
**Ted Young** 03:09 Cool.
**Ben Joseph** 03:11 Thank you.
**Ted Young** 03:13 Yeah, yeah, I was, joining just because there's also a Flutter effort, and I wanted to make the SwiftSig kind of aware that that was… That was going on. Here, let's… Meeting notes.
**Ben Joseph** 03:29 Bye.
Yeah, on the Android side, I think they are already aware, I think, the Flutter team tagged Android reviewers for some input.
Hoping they have some context.
I don't know if anybody has taken a look at it yet, though.
**Ted Young** 03:49 Yep.
Here… Send the meeting notes.
Might just be us.
**Ben Joseph** 04:56 I… I'm afraid.
Yeah. That's a case.
**Ted Young** 05:00 I'm curious, what's your impression of the state of Hotel Swift, since you're getting up to speed on the whole thing?
**Ben Joseph** 05:07 I haven't had a chance to explore much, but I'm told it's lagging behind Android a bit.
**Ted Young** 05:17 Yeah.
**Ben Joseph** 05:18 I have more, like, more familiarity with the Android, Hotel, SDK, and I've been, I've been, you know, already consuming that.
for some testing, I've been, like, building some consumer-side translations based on that.
On that front, like, we were discussing some, you know, label name changes, which were also not, like, strictly part of the semantic conventions, like, so how do we, you know, keep track of these changes? How does it affect consumers? Like, if you keep changing that between every minor version, like, this might be disruptive to consumers.
You know, I don't think we use the schema, you know, the auto schema, utilize that, like, we don't send it as part of the telemetry, the schema version. I think, not everything is part of the… you know, even if we are updating something, some of these things are not present in the previous semantic convention, so it's not one semantic convention to another, where I think that's where, like, we could actually use… make use of the, schema, Autel schema.
Cool. Or, translation. So, yeah, these are some of the challenges I saw with adoption and, You know, using these, the libraries as, as is today.
**Ted Young** 06:39 I think… And has Apple been involved? I know Alolita is normally the GC liaison, and she works at Apple, but I was curious if there's engineers from Apple at all.
**Ben Joseph** 06:52 I'm… I'm… I'm not aware. I… I… I… I just joined the last SIG meeting, and we didn't have anybody. I did not hear any updates about that. I think one of the major items we were discussing is the COCO ports deprecation.
So, that, definitely, I think we are going ahead and, like, plan to have the October like, have a last lease around October so that, like, we can… we have, we could, release up to December, so if there are any top fixes that we need.
That will give us 2 more months to, you know, deploy any fixes, and yeah, that would be the last one.
**Ted Young** 07:34 Okay, cool.
**Ben Joseph** 07:35 Yeah.
**Ted Young** 07:40 Mmm… Oh, I see someone else has joined.
Vinod?
You there?
**Vinod Vydier** 07:55 Oh, yes, sir. Hi, Ted. How are you?
**Ted Young** 07:58 Doing good, how are you doing?
**Vinod Vydier** 08:00 Good, good, long time.
**Ted Young** 08:02 Yeah, yeah.
Yeah, I was just joining the SwiftSIF just to kind of get up to speed with, you know, where y'all have been, and there's a sort of Dart Flutter effort, that's getting stood up, and since that's a cross, kind of cross-client effort, I thought it'd be good to raise awareness and… a good opportunity just to check in with you all and see how things are going over here in Swiftland.
**Vinod Vydier** 08:31 Yeah, that'll be great, and once we have, some of the hybrid, initiatives and… Because I think so far, we don't really have, support for… Anything in the… In the repo, right? We are… we already support Swift.
We don't support any hybrid or, Right. React Native, yeah, we've had a few requests before, React Native and Xamarin, what's the other one?
The new name for Xamarin?
**Ted Young** 09:07 Yeah, yeah, and it would be its own SIG, but, you know, it's one of those things where, you know, yeah, making sure there's… there's always, like, you know, every… every mobile and browser client, you know, does their own thing, but there's certain things where… We want to, like, maybe have some more cross-collaboration to make sure things work similarly across Across the different clients, and this seemed like a good example of We had kind of, like, shut down the client SIG after BrowserSig sort of spun out into its own group.
**Vinod Vydier** 09:40 Yeah.
**Ted Young** 09:41 wondering maybe this was, like, a good opportunity to start kicking off some of those, like, cross-client discussions again, seeing where the different SIGs are at, and, you know, other than session management, you know, just seeing what the list of things might be, you know.
**Vinod Vydier** 09:58 Yeah, we used to, I think, Bryce and a few times I have also joined the client's SDK SIG, and I think Bryce was, I think, more regular, and then Ari also joined a few times, not from the beginning, but I think, Yeah, like I said, there is still a lot of effort, right, in terms of, Having similar semantics across all these things, so that's… Yeah, yeah, still a work in progress, for sure, yeah.
I actually… I actually happen to be driving back from Gatlinburg, so that's why I'm not on video, but yeah.
I, I just stopped at a… Stoppedia and Milt.
I realize, I was running late for the sig.
**Ted Young** 10:49 Oh, okay. Well, if you're driving, we'll… we'll let you go. It's, it's just…
**Vinod Vydier** 10:53 I stopped for, I stopped to charge my car, so…
**Ted Young** 10:57 Okay.
**Vinod Vydier** 10:58 But I, I, yeah. You know, I was, I was gonna say, I don't… Our usual suspects are not, in today, so… Typically, it's Bryce, Ari, and Nacho and me, so, yeah.
**Ted Young** 11:17 Who from Apple is involved, by the way?
**Vinod Vydier** 11:21 So.
**Ted Young** 11:21 Or anyone worked.
**Vinod Vydier** 11:22 Yeah, so Apple… we've had Alolitas from the governance community, and she… she comes in… few times, I mean, she doesn't, join.
Most of the… but, she, she does, she's our, GC person.
And she's actually tried to bring in the Apple folks.
And we've had a few discussions with them Actually, this happens every once in 6 months.
Apple is interested, because they have, you know, instrumentation of their own, they have trace library and so on, and they want to collaborate, but it's… it's not been a regular thing. I mean, I wish they… they, you know, yeah, come in more often, they can take up some of the… workload and actually kind of merge the two efforts, right? But I think at least we have… we have some libraries where we can ingest people.
Swift, metrics from Apple. There's a Swift tracing library as well.
So, if you have a library, some sort of a bridge that we can… reduce some of that. So that would be a good effort, or, you know, things that we've been asking for.
And I think Apple is working on, you know, somehow… You know, combining some of those efforts, because as… OpenTelemetry becomes more prevalent, they want to, you know… being able to plug into the ecosystem, so yeah. So, Alunita is our point of contact, and… We've had a few Apple engineers join.
different Apple engineers, so, yeah, it's something that, We've been tracking that, for sure, yeah.
**Ted Young** 13:03 Okay. Well, maybe I'll come back next week when we've got more of our usual suspects and, and, poke on Slack, but I've been going around and poking. We do have, like, a client instrumentation Slack channel.
**Vinod Vydier** 13:18 Fantastic.
**Ted Young** 13:19 and we canceled the cross-client SIG meeting, but mostly I'm just going around and poking people, being like, hey, maybe this is an opportunity to… kind of reorganize that stuff. Also, in general, as part of our post-graduation roadmap, trying to think about how better to do project management in OpenTelemetry, and right now, you know, we have a technical committee, but the technical committee doesn't have a lot of, like, client-side expertise on it. We want to make sure all the different client SIGs are, like, well-connected with OpenTelemetry.
And, you know, have the ability to push through spec issues and things.
**Vinod Vydier** 13:56 That they can.
**Ted Young** 13:57 about.
So, yeah, that was just something, we can probably advocate better for what we want if we first talk amongst ourselves and kind of reassess, like, hey, what kind of, like, cross-client things would be helpful for us to coordinate? How would these different SIGs like to coordinate with each other?
**Vinod Vydier** 14:19 Pull you up, bud.
**Ted Young** 14:19 you know, how much do people have? Are there people working on the different SIGs who have some capacity to sort of look at the implementations, you know, across different languages? You know, like, just, like, what do we need to be doing to… to make sure that That it feels like a coherent effort, so…
**Vinod Vydier** 14:40 Yep, yep. Actually, Swift, is very much, So, from the Apple perspective ecosystem, we get most of the users or the requests coming in from the iOS side, right? Because.
**Ted Young** 14:54 Of course.
**Vinod Vydier** 14:54 It's more client-side, but the library itself is… Written in a way that is, You know, for server-side as well, right? So we don't have many users or requests coming in from there, but the challenge here is, you know, most of the semantic conventions in OpenTelemetry is more… heavily leaning towards the server side, right? So…
**Ted Young** 15:18 Yes.
**Vinod Vydier** 15:18 you know, as we add more, I think, yeah, this is… this would be definitely a place for us to… Yeah.
**Ted Young** 15:27 We add client-side semantic conventions.
you know, there's always that debate over, like, do we want to have, like, a cross-client convention, or is it better to have, like, you know, Android, iOS, you know, browser-specific conventions? It's always…
**Vinod Vydier** 15:45 Yo.
**Ted Young** 15:45 It's just like, do you want a database convention, or do you want a SQL convention, or do you want a Postgres and a MySQL convention?
**Vinod Vydier** 15:52 You don't think…
**Ted Young** 15:53 figuring that stuff out. And on the semantic convention side, you know, we're doing federated semantic conventions is a thing we're kicking off, like, giving… different groups more direct control over managing their semantic conventions. So, anyways, just a bunch of changes afoot that seemed like a good time to maybe reboot some cross-client effort.
**Vinod Vydier** 16:16 I think we do have some amount of, like, you know, like, device status and, like, network status, because these are all very important from a client's… perspective, right? From an iOS perspective, which is… Which is, I think, you know, something that is not… some of it is not formalized in the semantic conventions, but yeah, I think we need more of those.
Because there's a bunch of them that is, Very much, you know, important from a user perspective, from client, or the device perspective, right? And there's a lot of telemetry from the device that we can actually Select and, surface operate as a span attribute, so…
**Ted Young** 16:54 Absolutely. Yeah, the client mobile devices are different from servers, right? Like, they… we need different resources.
**Vinod Vydier** 17:01 Yeah, yeah. I mean, even as simple as, you know, like, You know, if the network is moving from… Wi-Fi to… 5G to 4G, or, you know, temperature, you know, things of that sort. All of that, actually.
In fact, it's the app, right? I was, The app that is running in the runtime.
So I think these are all things to track, yeah.
**Ted Young** 17:27 Yeah.
Okay, man, well, it was good catching up with you, it was good meeting you, Ben, as well.
But, yeah, I'll give you some time back and, pop over into that client, hotel client-side telemetry channel, and I'll be pinging people about it over the course of the next week, so… Okay.
**Vinod Vydier** 17:47 Alright, sounds good. I'll go on mute, you guys can continue.
**Ted Young** 17:51 Yeah, I think that might be it, it's just us, so, you know, probably just call it, I imagine.
Sounds good.
Unless you had something else you wanted to ask Finad, Ben?
**Ben Joseph** 18:07 Nothing for me.
**Ted Young** 18:09 Okay. Well, I'll see you all next week.
**Ben Joseph** 18:12 I did.
**Vinod Vydier** 18:13 See ya.
**Ben Joseph** 18:13 I even opened.
**Vinod Vydier** 18:14 That's… that's good.
