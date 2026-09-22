SIG: Networking SIG
Date: 2026-09-21
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Braydon Kains (Google LLC)** 01:42 Morning.
**Sven Cowart (ElastiFlow Inc)** 01:46 Hey, good morning.
How's it going?
**Braydon Kains (Google LLC)** 02:01 Not too bad, how you been?
**Sven Cowart (ElastiFlow Inc)** 02:03 Pretty good.
So what do you play, man?
**Braydon Kains (Google LLC)** 02:09 Mostly jazz.
**Sven Cowart (ElastiFlow Inc)** 02:11 Fun.
**Braydon Kains (Google LLC)** 02:13 I do play some… other types of stuff, I get hired for country gigs a lot. There's a lot of country stuff in Ontario.
**Sven Cowart (ElastiFlow Inc)** 02:19 Oh, okay. Where, where are you at?
**Braydon Kains (Google LLC)** 02:23 I'm in, Kitchener, Waterloo.
**Sven Cowart (ElastiFlow Inc)** 02:25 And where? Oh, oh, yeah.
**Braydon Kains (Google LLC)** 02:27 Yeah, so about an hour from Toronto.
**Sven Cowart (ElastiFlow Inc)** 02:30 Have you, heard of… Krantz?
**Braydon Kains (Google LLC)** 02:34 Wayne Cranz, the…
**Sven Cowart (ElastiFlow Inc)** 02:36 Yeah.
**Braydon Kains (Google LLC)** 02:37 Yeah, yeah, he's great.
**Sven Cowart (ElastiFlow Inc)** 02:38 I just got into them this weekend. Krantz, the Krantz car lock and left… I don't know, LeftBriv?
Album?
**Braydon Kains (Google LLC)** 02:46 Oh, yeah. It's really good.
**Sven Cowart (ElastiFlow Inc)** 02:52 I've, I play, I don't say I play jazz, but I like jazz a lot, and I, dabble in it every once in a while, but I play mostly, like.
versions of extreme metal, more like progressive metal, but…
**Braydon Kains (Google LLC)** 03:06 Yep. I don't know if you… I listen to a lot of that stuff, I don't really play it.
**Sven Cowart (ElastiFlow Inc)** 03:10 Do you… I'm sure you know Mushuga.
**Braydon Kains (Google LLC)** 03:12 Yep.
**Sven Cowart (ElastiFlow Inc)** 03:13 And Frederick?
And, like, Frederick sends me down rabbit holes of… Various jazz artists to explore, so… and I really enjoy that type of music.
I'm actually taking a course right now on Josh Mader.
Which… I don't know if you've heard of him, but he's really good.
**Braydon Kains (Google LLC)** 03:31 pregnant.
**Sven Cowart (ElastiFlow Inc)** 03:32 He's a newer guy, younger person, but he released an album called Ultraviolet, you should check it out, it's really good.
And…
**Braydon Kains (Google LLC)** 03:43 Oh, I think I've… I've seen this album cover in my, like, release radar thing.
Yeah, that's awesome. Yeah, I'll take this up.
**Sven Cowart (ElastiFlow Inc)** 03:51 Yeah, you should check it out.
It's my… it's actually the first song the… the… the title of the album's called Ultraviolet, the first song's Ultraviolet, and it's what my son goes to sleep to. He's, 15 months old. It's pretty bizarre that that's the one that gets him to sleep.
Okay, I'm… Let me ping Antonio, because he's got quite a few talking points here.
Looks like people are lagging behind today.
Well, while I have you here, I actually need a… I need a favor.
From you on… This… The add cross-layer Guidance.
**Braydon Kains (Google LLC)** 04:47 Oh, yes, the one… That covers system stuff, right? I saw… I saw that when you posted it last week, Ivan.
**Sven Cowart (ElastiFlow Inc)** 04:56 Yeah, yep. I… last thing I was just asked was a… Was a review from Security and System SIGs.
**Braydon Kains (Google LLC)** 05:03 Okay.
**Sven Cowart (ElastiFlow Inc)** 05:04 I don't think there's really a… I think it's important that you… you read it, but I don't know if it… it doesn't talk about the system's area.
But obviously you guys use… I think you prefixed, right, network.local?
**Braydon Kains (Google LLC)** 05:21 Yeah, I think so, for the metrics that measure, like, interface… Yeah, I think.
**Sven Cowart (ElastiFlow Inc)** 05:28 Yeah, so just make sure that that part, I guess, is correct. I didn't change any of the definitions here, so I did slightly tighten the source and destination definition, and then just made it clear on what each represents.
But yeah, if you could get that, that would be really useful for me.
The other one I did, which probably also maybe has an impact on you… But this is, came out of some work. I'm trying to… for the OBI group, there is… this ticket I created a while ago, when it was donated, they were still using some…
**Braydon Kains (Google LLC)** 06:09 Hmm.
**Sven Cowart (ElastiFlow Inc)** 06:09 some anti-conventions that doesn't actually exist in OTEL, and I've been trying to push to get some anti-conventions On their project that, exists in OTEL, and so I've been trying to make changes here. One of the problems is with Weber now.
that… The network transport and network type properties are too small.
So they had to do a bunch of custom overrides, and this is going to become a problem for me as well.
When I donate the work I did on a project called Mermin, to OBI, but this… all this does is expand the, the types listed.
in the enum, so that Weaver won't complain, and I just identified the most common That are often used in network observability in both.
I think I made a copypasta error here, because this is not right.
They can't both be the same.
**Antonio Martinez (Cisco Systems, Inc.)** 07:05 Okay.
**Sven Cowart (ElastiFlow Inc)** 07:06 Let me fix that real quick.
**Antonio Martinez (Cisco Systems, Inc.)** 07:08 There is a small difference, but they are pretty much the same in the description.
The only one that changed is the…
**Sven Cowart (ElastiFlow Inc)** 07:17 I think I just copy and pasted it in the wrong thing, because I… I reworded it, and…
**Antonio Martinez (Cisco Systems, Inc.)** 07:23 Excel later, could be.
**Sven Cowart (ElastiFlow Inc)** 07:25 Yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 07:25 Cooling.
So, for me, about that pull request, the only thing that was a little bit confusing was.
You said it could be used for… let me read it here… 2020 second.
Because every time, for example, for the… Destination address.
I'm trying to look.
For over your scene.
Okay, I opened the Grand PO, give me a second. Here it is.
**Sven Cowart (ElastiFlow Inc)** 08:08 Sorry, say that again?
**Antonio Martinez (Cisco Systems, Inc.)** 08:08 Madoka.
Yeah, let me, let me try to find out where you're seeing the…
**Sven Cowart (ElastiFlow Inc)** 08:29 Thanks for that.
**Antonio Martinez (Cisco Systems, Inc.)** 08:36 Yeah, this is what I'm trying to say. Okay, for example, for the network type, you're saying Ethernet type of the observed frame Or… Aussie Network Layer, or non-USE equivalent for non-FML network. What I am saying is, like.
we were supporting only the Aussie network layer, which was IPv4, IPv6, from an IP point of view.
For the network type, but now we are also supporting the… as you were saying, the ethanotype. Could make sense to create, like, a… new attribute for the FNF type. I have the feeling that they… I am fine with both together, but is it, like, a timing when we want to use both attributes? Like, I want to be that IPV for something else?
from the ethnic type.
Or that will never be this case.
**Sven Cowart (ElastiFlow Inc)** 09:37 Well… I don't… Say that last part again, so I make sure I understand. You're saying, yeah, just say it again.
**Antonio Martinez (Cisco Systems, Inc.)** 09:49 You are somehow reusing the network type for what it was before, it was OC Network Layer, and now you are also using it for SMET type.
I am fine with that goal, but now that… attributes have two meaning. One could be, like, Aussie, or one could be SMAT type. Would that make sense to create, like, a new attribute?
And keep it as it was already stable, the AP before EPV6? Or did you evaluate that, or have you thought about that?
**Sven Cowart (ElastiFlow Inc)** 10:20 Well, but I… I don't think that's… that's true, though, because there's actually… So… There's the Ethernet-type IPv4, IPv6, that was there before.
**Antonio Martinez (Cisco Systems, Inc.)** 10:34 Correct.
**Sven Cowart (ElastiFlow Inc)** 10:35 Under type.
So, it was always my assumption, because they list TCP UDP here, that this was talking about the ether type in L2L3.
**Antonio Martinez (Cisco Systems, Inc.)** 10:47 Okay.
**Sven Cowart (ElastiFlow Inc)** 10:48 And…
**Antonio Martinez (Cisco Systems, Inc.)** 10:49 Period.
**Sven Cowart (ElastiFlow Inc)** 10:49 This is relisted for IP and IP.
Right, because, like, L4 header.
After the ether header, And it varies… Header extensions can be… the protocol on IP headers, right? So if you have IPv4, IPv6, the protocol on that can be IPv… again, IPv4, IPv6, but that's not an ether type at that point anymore.
Is that what you're saying?
**Antonio Martinez (Cisco Systems, Inc.)** 11:19 Yeah, kind of, and that was a little bit confusing for me, yeah.
**Sven Cowart (ElastiFlow Inc)** 11:22 Yeah, yeah, it is really, Let me… this is actually easiest to show if, Would it help if I show a PCAP of that?
Real quick?
Let me do that real quick. I'll open up Wireshark here with an example.
**Antonio Martinez (Cisco Systems, Inc.)** 11:46 Kronos.
**Sven Cowart (ElastiFlow Inc)** 12:00 For some reason, I can't find… the Zoom bar.
on my screen.
So I don't know how to shop sharing right now.
What's going on here? Oh, there it is.
Okay.
Let me share… Yes.
So this is what I'm… this is IPv4 inside of IPv4.
So you have your frame 1, right?
And then you have the ether header.
It always comes this way. And then here you have the Ether-type IPv4.
**Antonio Martinez (Cisco Systems, Inc.)** 12:38 the network type.
**Sven Cowart (ElastiFlow Inc)** 12:39 Yeah, so that's network type, and then you have… the IPv4 header, Which has a protocol, Love… That is a bad explanation of that, because that matches to, IPv4 type, you can see that here, so if I go to the… the… Ayena.
Transports… Sorry, I have to switch… I'm jumping all over here, I'm sorry about this.
Right, but the value here is 4, so the keyword's actually IPv4.
And that's the same thing.
is… this… IPP4, IPv4 header. That's why it says IPIP, and the value is 4.
Because this is an IPV.
**Antonio Martinez (Cisco Systems, Inc.)** 13:30 before?
**Sven Cowart (ElastiFlow Inc)** 13:31 Protocol header, and then you get your… another IPv4 header where the protocol is actually UDP.
**Antonio Martinez (Cisco Systems, Inc.)** 13:41 And then we will put, for the transport, we will put UDP in that scenario.
**Sven Cowart (ElastiFlow Inc)** 13:45 Yes.
Yep.
Because the… the extra call-out here… is that… in… This guidance, do-doo… So… and make a specific call out here, that if it's IP and IP, or any of these encapsulation protocols, you choose the inner protocol.
**Antonio Martinez (Cisco Systems, Inc.)** 14:21 sure.
**Sven Cowart (ElastiFlow Inc)** 14:24 Unless… and so this is a lot of… just for redundancy, or if the instrumentation, for whatever reason, can't go deeper than one packet, or one… Ether header down, right? So, yeah.
Does that… does that clear up what… what you were asking?
**Antonio Martinez (Cisco Systems, Inc.)** 14:42 Yeah, yeah, it's more clear enough, awesome, yep.
**Sven Cowart (ElastiFlow Inc)** 14:44 Okay, cool.
Hey Yash, sorry, I just noticed your hand was up.
**Antonio Martinez (Cisco Systems, Inc.)** 14:58 I think she has a question on the Google Drive.
**Braydon Kains (Google LLC)** 15:01 I've answered it directly in the doc.
**Sven Cowart (ElastiFlow Inc)** 15:04 Old.
Okay.
**Braydon Kains (Google LLC)** 15:06 I just wrote an answer.
**Sven Cowart (ElastiFlow Inc)** 15:11 I see.
Cool. Alright, so, yeah, so those are there.
Antonio, I finally, I think, have the final place for the guidelines, so that's good there, but I just need a couple more reviews from… one from the system SIGs, which Braydon will help us with, and then one from the security SIG. I'll attend the Security SIG call to bring this up to them, because I didn't get a response on…
**Antonio Martinez (Cisco Systems, Inc.)** 15:35 Do you… do you make sense to merge your prerequests first after the two pre-requests that we have open, I understand? Because I think we are… you are moving the structure.
I don't know how… I mean, you will need, if not, to fix conflict later, naturally.
**Sven Cowart (ElastiFlow Inc)** 15:53 I don't think I move…
**Antonio Martinez (Cisco Systems, Inc.)** 15:58 Okay. It should.
**Sven Cowart (ElastiFlow Inc)** 16:00 Didn't have an impact.
Cause it's just changing, yeah.
It's just changing some of the words here.
Maybe there will be, but… I mean, I would like to get this merged as soon as possible, but it's… it's dragging along right now, so… but I think it's ready.
**Antonio Martinez (Cisco Systems, Inc.)** 16:14 Yeah, it's fine.
Yeah. There's my kids are on there.
**Sven Cowart (ElastiFlow Inc)** 16:18 Okay, let's spend a couple more minutes looking at these.
Oh, yes, alright, I think then we would probably get into the topics.
One favor here, Antonio, for you.
The… before you joined, I don't know if you caught that part, I was explaining to Braydon I'm trying to help them, the OBI.
team resolve.
Did you hear that part?
**Antonio Martinez (Cisco Systems, Inc.)** 16:56 No, no, no, no, I just seen when you were talking about the type, not what type.
**Sven Cowart (ElastiFlow Inc)** 16:59 Okay, so the… I'm trying to help them resolve some of the problems they have with their schema, because they still use, when it was donated, when Bayo was donated to OpenTelemetry and became OBI, they still use some of the old semantic conventions on the attributes, and so I'm trying to transform them. Obviously, there's, CIDR here, right? Which, that's something that we also want.
It kind of really.
**Antonio Martinez (Cisco Systems, Inc.)** 17:25 Alright, but we… we are proposing to call it prefix, or maybe cider is also fine for me, honestly, I don't have a strong opinion.
What about that?
**Sven Cowart (ElastiFlow Inc)** 17:34 They'll adopt whatever we decide on. I don't think that's… so whatever one we think is stronger, but it would be good to,
**Antonio Martinez (Cisco Systems, Inc.)** 17:43 Nope.
get it working. Feel free to put that into… to do anything to me, I can do it again.
**Sven Cowart (ElastiFlow Inc)** 17:48 Cool, thank you.
Quiet.
**Antonio Martinez (Cisco Systems, Inc.)** 17:54 I can, I can, I can do it myself.
That's good to know.
**Sven Cowart (ElastiFlow Inc)** 17:58 Oh, there we go.
Okay, you got it. Cool.
Awesome, thank you.
**Antonio Martinez (Cisco Systems, Inc.)** 18:07 But how do we… how do we tackle? For example, for that one, we don't have yet a… Decision, if we are gonna call it cider, or… we are gonna call it prefix. I'm more in favor of prefix from my point of view, but should I create a pull request and decide there, or… I imagine that's the way to go, right?
**Sven Cowart (ElastiFlow Inc)** 18:27 Let's… Well, there's already a number of things happening here.
**Antonio Martinez (Cisco Systems, Inc.)** 18:36 I mean, all of those are from June 1, so it's a little bit outdated.
**Sven Cowart (ElastiFlow Inc)** 18:40 Yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 18:40 none.
**Sven Cowart (ElastiFlow Inc)** 18:45 I would be fine if… to open a PR and just make the best recommendation.
This, though, does get into the area of, and I don't know if you solved for this, Where… Like, yeah, we can add these things to peer, but we also need to add it to source and to client.
**Antonio Martinez (Cisco Systems, Inc.)** 19:05 Correct, correct, and…
**Sven Cowart (ElastiFlow Inc)** 19:06 Yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 19:08 I'm doing two all of them, yeah.
Input request.
**Sven Cowart (ElastiFlow Inc)** 19:12 Oh, you had that?
**Antonio Martinez (Cisco Systems, Inc.)** 19:14 Yeah, if you go to the second one, I think that's a poor question.
**Sven Cowart (ElastiFlow Inc)** 19:21 Awesome. Okay. Yeah, so that'll be treated the same way, I guess, then.
**Antonio Martinez (Cisco Systems, Inc.)** 19:26 Okay, no.
**Sven Cowart (ElastiFlow Inc)** 19:29 Okay, do you want to walk through yours, then?
**Antonio Martinez (Cisco Systems, Inc.)** 19:32 The first one was related to your request, if we get any updates, if I'm not mistaken.
**Sven Cowart (ElastiFlow Inc)** 19:37 I see.
**Antonio Martinez (Cisco Systems, Inc.)** 19:38 Yeah, and you already clarified, so it was more a follow-up. The next one is the ASN pull request that I just stuck.
So whenever you guys find out time, please take a look, and I do have also a question right on that this year, that's really cool. So we have approval privilege, but I don't think we can merge requests, so once we get approved by any of us, we will go to… the semantic commission team to merge it, right? Or what should be the approach here?
**Braydon Kains (Google LLC)** 20:05 Only the maintainers can merge.
So they… they usually wait for the approver group to say something first, generally, and then the, general SEMCOF… there's… so there's the area approvers, then the general, like, SEMCOMF-wide approvers, and then the maintainers.
Usually they'll wait for the specific area code owners to say stuff.
so the specific area approvers, and then Either general semantic approvers or maintainers will look, and then maintainers can merge once They've gotten approval for both the area and from the general SEMCOP approvers.
**Antonio Martinez (Cisco Systems, Inc.)** 20:44 And you are a maintainer right now?
**Braydon Kains (Google LLC)** 20:46 I am not.
Okay.
**Antonio Martinez (Cisco Systems, Inc.)** 20:50 So we need to ping other people for that?
**Braydon Kains (Google LLC)** 20:53 I am on the same team with two maintainers, so I can… I can DM them, but…
**Sven Cowart (ElastiFlow Inc)** 21:01 Is that Lude, Milla, and Josh?
**Braydon Kains (Google LLC)** 21:02 Yep.
**Sven Cowart (ElastiFlow Inc)** 21:05 It seems like, now that Josh isn't… is Josh… Josh is not a maintainer anymore, is he? Of the Cemcom group?
**Braydon Kains (Google LLC)** 21:12 I don't know, I thought he was still a maintainer of the repo. He stepped down from the technical committee.
**Sven Cowart (ElastiFlow Inc)** 21:20 I see.
**Braydon Kains (Google LLC)** 21:21 I thought he was still the maintainer of the repo, but I haven't been keeping track.
**Sven Cowart (ElastiFlow Inc)** 21:24 I see. Okay. Yeah.
**Braydon Kains (Google LLC)** 21:25 I'm talking to him later today, I can ask, but…
**Sven Cowart (ElastiFlow Inc)** 21:27 Okay.
Antonio, so Ludimilo's our TC, so she's always going to be helpful, and then, Thrask is the other person that seems Like, he does a lot of the approvals and getting things in, and Recently, I've been interacting with… His name's escaping me.
**Antonio Martinez (Cisco Systems, Inc.)** 21:52 Yeah, I saw… Yeah, good.
**Braydon Kains (Google LLC)** 21:55 Oh, yeah, Christoph, yeah, he's a…
**Antonio Martinez (Cisco Systems, Inc.)** 21:57 Yeah.
**Braydon Kains (Google LLC)** 21:59 Actually, he might be a maintainer. He might be able to merge. I forget if he got promoted to maintainer. He was… he was a, like.
A repo-wide prover for a while.
**Sven Cowart (ElastiFlow Inc)** 22:09 Oh.
**Antonio Martinez (Cisco Systems, Inc.)** 22:10 Nice, nice. Okay, yeah, I will ping him also, I remember him from last WivCon in person. Okay.
That's great. So, that's also my status. I would also work on the MAC address that I couldn't… I couldn't make it on time for this session, but yeah, we'll work on that. And that's your… your pull request, and I wanted to comment that because of that comment.
**Sven Cowart (ElastiFlow Inc)** 22:31 Okay.
That makes sense.
**Antonio Martinez (Cisco Systems, Inc.)** 22:33 Yeah, that's right.
**Sven Cowart (ElastiFlow Inc)** 22:34 Okay, awesome.
And…
**Antonio Martinez (Cisco Systems, Inc.)** 22:40 So that's my to-do that, for the prefixes.
Do you mind also linking to me, or passing to me on a Slack? Write that one, so I will try to coordinate another comment that we are working on that.
**Sven Cowart (ElastiFlow Inc)** 22:56 Yo.
**Antonio Martinez (Cisco Systems, Inc.)** 22:56 How is the… how is the status on the OVI team on that? Are… are they already doing and released the… the attribute, or are they already… still on a… oh, this is open, okay.
**Sven Cowart (ElastiFlow Inc)** 23:07 Yep. So…
**Antonio Martinez (Cisco Systems, Inc.)** 23:08 They hung up.
**Sven Cowart (ElastiFlow Inc)** 23:09 this. They're all for it.
They… originally, the goal was to get this in Before they change to V1.
And, you can see I created this a while ago, and I've just been trying to get my bearings this year getting into OpenTelemetry, so, here we are, way too late in the year, so it might not make it in with V1, but they're still open to having… having it merged as soon as possible.
I wanted to do it quickly because that… it would… to avoid a braking change for them, because I believe that would be a braking change.
So, the sooner the better, but there's an… I need to create another follow-up issue, because there's more than just these that I've now found when I was working on this on Friday in the OBI repo that need to be aligned to specific OTEL conventions.
**Braydon Kains (Google LLC)** 24:02 I wonder if they have a mechanism, like, in the collector with, like, feature gating, or, like, being able to… Turn on and off features based on command line flags or something when you start OBI. I assume, obviously, the eBPF artifacts can't… Take options like that, so it's kind of hard to say whether that's possible or not.
**Sven Cowart (ElastiFlow Inc)** 24:24 Oh, you… you could. You could. It's just… Yeah, no, you definitely could, because there's a user side.
user space side to the eBPF8 program, so…
**Braydon Kains (Google LLC)** 24:35 Thank you.
**Sven Cowart (ElastiFlow Inc)** 24:35 all that kind of stuff. You should be able to, I just don't know where they are with that kind of feature. I'm still learning.
**Antonio Martinez (Cisco Systems, Inc.)** 24:41 You're… Giuseppe, you're from the OVI team, right, Giuseppe?
**Giuseppe Ognibene | Coralogix** 24:46 Yes.
**Antonio Martinez (Cisco Systems, Inc.)** 24:47 Yep, bro.
**Giuseppe Ognibene | Coralogix** 24:48 I was… I was looking to reply to you, but I'm not sure about that part. We have the features flag.
But I don't… I don't think you… you were talking about it.
**Braydon Kains (Google LLC)** 25:00 I was just thinking, because the way the collector handles this is when we… Try to shift a receiver to the, like, semantic conventions… schema, like, we make a full breaking schema change over to the semantic conventions version. We have a standard set of feature gates that people can set when they start the collector to say.
produce the SEMCOMF schema versus produce the old schema. Something like that might be useful for… for something like this, versus having to decide when to just merge the breaking change and… and… Let it all happen at once.
That might… that might be helpful, if that sort of thing was possible through… through OBI.
**Giuseppe Ognibene | Coralogix** 25:41 Okay.
I… I'm not sure about that.
Again, again, try to ask.
**Braydon Kains (Google LLC)** 25:51 Either way, whatever… Whatever works. It's… It's just a matter of, it's up to the OBC how you want to handle this. It's just… the way the collector's handling this now is… we're kind of… Making a philosophical adjustment to say that, like, as we cut things for 1.0, we're gonna kind of accept a lot of the, like, non-Semconv stuff that people are producing as, like, de facto standard. Like, the host metrics receiver has been producing the same, not semantic conventions, viable metrics for ages.
People have been running in production for a long time.
If we're gonna mark… we're gonna… if we wait to mark V1 for, like, when SEMCOM is ready, it'll take forever.
So… We're, we're sort of… changing to, like, we're gonna mark things as stable, kind of, as they are today, and, like, the V2 shift is when the semantic conventions change happens, so… OB… OBI could… adopt a similar… a similar concept, where you decide to mark V1 with what you have, because enough people… a sufficient number of people are already running in production, relying on the existing schema.
And then, if you could introduce it, like, optionally introduce SEMCOMF, during V1, then when you decide to make, like, a V2 bump, that's when you decide, like, okay, the new default is the SEMCOM version.
But that's up to.
**Antonio Martinez (Cisco Systems, Inc.)** 27:25 Super beard here.
**Braydon Kains (Google LLC)** 27:26 That's just… that's just the way Collector's doing it, is going to be doing it going forward.
**Antonio Martinez (Cisco Systems, Inc.)** 27:35 else.
**Sven Cowart (ElastiFlow Inc)** 27:36 on that topic, Giuseppe,
**Giuseppe Ognibene | Coralogix** 27:39 Yep.
**Sven Cowart (ElastiFlow Inc)** 27:40 Where… What's the state of this, and… Seems like it's stalled a little bit.
**Giuseppe Ognibene | Coralogix** 27:47 Yeah, that's… that's a very long topic for me.
I remember that I had a discussion with Rob about some, some metric that I wanted to add.
I didn't have the time, actually, to… to implement these metrics.
Well, actually, I implemented some days ago the TCP successful connection.
I don't know what you want to do. I can try to split it in sub-issues, but…
**Antonio Martinez (Cisco Systems, Inc.)** 28:22 Maybe.
It's Rakuten.
To check it out more.
**Giuseppe Ognibene | Coralogix** 28:28 Yeah.
**Sven Cowart (ElastiFlow Inc)** 28:33 So is there…
**Giuseppe Ognibene | Coralogix** 28:33 it's built.
**Sven Cowart (ElastiFlow Inc)** 28:34 You're saying that…
**Giuseppe Ognibene | Coralogix** 28:35 Maybe not.
**Sven Cowart (ElastiFlow Inc)** 28:36 Part of the work is done, but… Not all of it, is that what you're saying?
**Giuseppe Ognibene | Coralogix** 28:42 No, I mean, if you go… if you go up, there is a list of metrics that I implemented in Obi.
And a list of metrics that I would like to implement.
For example, I added TCPRTT, and with Rob, we had a discussion about the… the… let's call it, the hook point, I mean, not the hook point, the value of the TCP SOC that I was using it, but this is a, let's say, a deeper discussion.
the, I'm gonna say, briefly.
I wanted to add this, this matrix, just to be compared to the semantic information, because there are no matrix like that.
**Sven Cowart (ElastiFlow Inc)** 29:28 I see.
**Giuseppe Ognibene | Coralogix** 29:29 But I… when I started, there was no network group.
**Sven Cowart (ElastiFlow Inc)** 29:35 Yeah.
**Giuseppe Ognibene | Coralogix** 29:37 that… That's why it was installed.
Yeah, so I was talking about this, this graph, graph here.
**Sven Cowart (ElastiFlow Inc)** 29:46 And I'm assuming, partially, it's… would it be fair to say that it's blocked because we don't have the entities defined for this yet?
**Giuseppe Ognibene | Coralogix** 29:55 Yeah. Let's say that I added some matrix that I was… I'm gonna say, pretty sure, or that, We, we needed for some customers.
And, but then I decided to stop also because, I didn't want to do, like, Added a metric then change it, did a breaking change, and…
**Sven Cowart (ElastiFlow Inc)** 30:20 Yeah.
Yeah, that makes sense.
Alright, so… I think then the issue, because I think you're… you're probably right, that these metrics… I haven't looked that detailed into it.
But we need these metrics, but the problem is that We need the semantic conventions first.
**Giuseppe Ognibene | Coralogix** 30:44 Yeah.
**Sven Cowart (ElastiFlow Inc)** 30:47 Wish that makes sense.
It's kind of the same problem I have. So… Oof.
Can you do this? Just cause it's… might be a little bit hard to follow here?
**Giuseppe Ognibene | Coralogix** 31:02 Would you…
**Sven Cowart (ElastiFlow Inc)** 31:02 But another issue that just says, these are the semantic conventions that we need, 2… Close this.
And then we can work that, or just make a comment. Actually, comment's probably better. Just add a comment.
explicitly stating the semantic conventions you believe are missing?
Complete this.
**Antonio Martinez (Cisco Systems, Inc.)** 31:27 Also, another comment, we already took the decision that we are not going to use System. It was, like, a sort of legacy… On the… from the semantic convention, so every system.network, it's not something that we're gonna keep adding and doing it anymore.
**Sven Cowart (ElastiFlow Inc)** 31:44 Yep, that makes sense.
**Giuseppe Ognibene | Coralogix** 31:46 So, Sven you mean that, I need to add a comment? I mean, when you say it's missing the semantic convention, you mean some, attributes or, anything else, just to… okay, okay.
**Sven Cowart (ElastiFlow Inc)** 32:00 Yep, and, maybe… I mean, I don't know if you know, but… If you have any ideas on what entity this relates to.
I know it's… we're early in that discussion, But I think that would be helpful to just call that out. I mean, I suppose… I guess, is this the list, actually, now that I'm looking at this again?
**Giuseppe Ognibene | Coralogix** 32:28 Yeah, this is the list.
**Sven Cowart (ElastiFlow Inc)** 32:29 Okay, so never mind. I just need to read the whole issue.
**Giuseppe Ognibene | Coralogix** 32:34 I think that you… I think that you just need to read, like, the initial issue, not my discussion with Rob, that… Okay. Related to…
**Sven Cowart (ElastiFlow Inc)** 32:45 Okay, let me get back into this, then.
See how we can move this forward.
**Braydon Kains (Google LLC)** 32:51 Whether to use the system namespace, usually we would only use the system network namespace if it's something specific about, like, the system's network interfaces. So, like, when we're measuring, like, packets on a network interface on a, like, a VM or something, that's probably the only case we're gonna keep system network around.
Otherwise, like, if this is just measuring… TCP on, like.
any kind of device or on, like, an application server or something like that, we would keep it in network rather than system network. I assume the system network is here because there probably are some still remaining that Or at least there definitely were at the time, some system network stuff that should not have the system prefix and just did for legacy reasons, and we can… Work.
**Giuseppe Ognibene | Coralogix** 33:37 Yes.
**Braydon Kains (Google LLC)** 33:38 Get rid of that, but…
**Giuseppe Ognibene | Coralogix** 33:39 Yeah, yeah. I wrote it in the description.
I mean, I decided to add it in system for various reasons, but yeah.
That was the… the summer.
**Braydon Kains (Google LLC)** 33:50 I would say a lot of the stuff that's in System.network right now Probably doesn't make sense.
**Giuseppe Ognibene | Coralogix** 33:56 Yes, okay. Okay, I agree with you, yes.
**Braydon Kains (Google LLC)** 34:00 Yep.
It was just because the history was that these metrics started in the host metrics receiver, is where the first time a lot of these, like, network metrics were being defined.
And back then, anything that came out of the host metrics receiver was just called system… had a system prefix no matter what. And so we ported it from there initially, but then this… I sort of brought in this concept of, like, we should only have things under a system namespace if it's going to relate to, like, an actual operating system, or, like, an actual machine, like, that is the way that system makes sense, and so I'm still working on untangling a lot of that historical, just, like, system namespace is just there, because that's where System puts stuff.
So, still working on that, but…
**Sven Cowart (ElastiFlow Inc)** 34:47 Braydon, I… maybe you can help me understand, because this is one point where I'm a little confused by that still, and it's probably why there is this tangling.
So from… and maybe, Giuseppe, you have a good answer to this, but… These metrics are, being generated from an eBPF agent.
that… So, it is, in fact, being generated from the system and about the system, right? Because it's running in the kernel.
**Giuseppe Ognibene | Coralogix** 35:17 I… I have my… I mean, my idea is that the, I was gonna say. I mean, the metric should not have been decided from, I mean, okay, we… I'm… I'm creating, I'm calculating the TCPRTT using a BBBF program.
But the definition of the metric should not have been… I mean, should not have considered the fact that I'm using eBPF.
The fact that.
**Antonio Martinez (Cisco Systems, Inc.)** 35:47 I'm…
**Giuseppe Ognibene | Coralogix** 35:47 other dating system is just because It's for… it's a not-wide metric.
**Sven Cowart (ElastiFlow Inc)** 35:56 I see. So, yeah, that makes sense, so they can be reused outside of it?
**Giuseppe Ognibene | Coralogix** 36:02 Yes, exactly.
**Sven Cowart (ElastiFlow Inc)** 36:02 Yeah.
**Giuseppe Ognibene | Coralogix** 36:03 Otherwise, it's just related to Obi, and I don't think that… demanding convention is, I mean, I think that, some of this metric you can, use other tools to calculate it.
Not… not related to eBPF.
**Sven Cowart (ElastiFlow Inc)** 36:20 Got it.
**Braydon Kains (Google LLC)** 36:20 I think, yeah, like, reading these metrics, I'm still not quite as much of a networking expert as everyone else in the group, but from what I'm reading.
I feel like these metrics, like, they could apply to like, what a network interface on the system has, like, received overall, but they seem like they could also apply to just, like, any TCP application that is a server. Like, it probably is… can also track things like… RTT and current connections and stuff like that.
**Giuseppe Ognibene | Coralogix** 36:52 Yes, yes.
**Braydon Kains (Google LLC)** 36:53 So I think that that would be a reason to take it out of the system namespace. I think the system namespace is reserved for, like.
the only way this metric semantically makes sense is if I'm talking about measuring it from an operating system perspective, whereas these metrics could be used to describe that, but also could be used to describe more generic stuff.
**Sven Cowart (ElastiFlow Inc)** 37:13 Yeah, I…
**Giuseppe Ognibene | Coralogix** 37:15 The.
**Sven Cowart (ElastiFlow Inc)** 37:16 That last part makes sense. The part where that breaks apart for me is that Is maybe the reference or relationship to network interface?
Because… All of these are only possible, obviously, if there's a network interface.
Like, what the hell.
**Braydon Kains (Google LLC)** 37:34 Yeah, right, if there is a network interface, it's the only way you can get this stuff. Yeah. Like, the TCP connections and stuff are possible only because of a…
**Sven Cowart (ElastiFlow Inc)** 37:44 Yeah.
**Braydon Kains (Google LLC)** 37:44 Network interface, like… so I guess… the… the reason I would say it's… these aren't in system is because It's…
**Giuseppe Ognibene | Coralogix** 37:58 If…
**Braydon Kains (Google LLC)** 37:58 We couldn't use these metrics to describe only reading and network, only.
**Sven Cowart (ElastiFlow Inc)** 38:03 Yeah. That makes sense, not the operating system side of it.
**Braydon Kains (Google LLC)** 38:07 Yeah, I try to keep the system namespace reserved for, like, This is… like, they're, like… so this might not be a real scenario, I'm just making one up for the sake of it, but imagine there was something about TCP metrics specifically when you're measuring it, like, the actual network interface level, that is semantically different than if you were reporting it for, like, a TCP server, like, specific application.
Or, like, maybe on, like, router hardware or something.
And if that existed, then you would put it in system.
So that it can be semantically differentiated from the generic. Like, if round-trip time, for some reason, when you're measuring it on an interface, it was different in the… in terms of the implementation, in terms of what the metric means, or, like, the design of the metric.
What… what may shake out to be true as we bring in network experts who can tell us more about what this stuff means, there may be no system.network in the end. It may come out that there is nothing… this scenario that I'm describing, that I'm trying to keep open as an option, just doesn't make sense, and so we just take everything out of system.
Yep, that's.
**Antonio Martinez (Cisco Systems, Inc.)** 39:22 Am I going like this.
The namespace should not be system.network. That's my opinion, too.
**Sven Cowart (ElastiFlow Inc)** 39:30 I… That's kind of… that's kind of where… based on what you just said, Braydon, that's kind of where I'm leaning. But look, let me do this. I'll open an issue about it, and we can just have a conversation about it.
**Braydon Kains (Google LLC)** 39:43 Yeah, I think if you… if you open an issue, and I'll put my… my explanation as a comment on the issue, and then, like.
I… I don't want System.network to exist just for the sake of existing. I'll explain the reason that I want to leave the option open, and then if that option never makes sense, then we take everything out of system.network. That is fine with me.
**Sven Cowart (ElastiFlow Inc)** 40:08 Okay.
Awesome.
**Giuseppe Ognibene | Coralogix** 40:10 Braydon, just to be sure, if you go to read the description, there is why I added it inside the system network. I mean, because I saw that System Network was having only metrics about like, NIC-level counters.
But I agree with you. Then, if you go to read also Rob's comments, we were talking about, like, the point at which you measure the same metric. Like, you were talking about RTT, you can measure it at different parts of the networking stack.
So, it can be inside system or not. That is a question that I can't answer right now.
**Braydon Kains (Google LLC)** 40:57 Yeah, I think that… so that's an example where, like.
I would… whether we keep a system network namespace around basically depends on Imagine a user sending to some metric backend.
would they want… Two different time series… So, like, if someone was measuring it at the interface controller level, or someone was measuring it at an application level, or somewhere else, would they want those things to be distinct in their backend, so that they can make dashboards that make sense? Because if you're measuring it at one point, and that semantically changes how we design the time series.
then we would probably want to name it differently so that it's obvious, but if… If us measuring it at an interface controller level versus at an application level or somewhere else can be purely defined by, like, just an enum attribute that makes it clear.
then…
**Giuseppe Ognibene | Coralogix** 41:55 Excellent.
**Braydon Kains (Google LLC)** 41:55 that's enough, I think.
**Giuseppe Ognibene | Coralogix** 41:57 Yeah, yeah, that's exactly our discussion.
Yep, good.
**Braydon Kains (Google LLC)** 42:05 Yeah, unfortunately, I don't know enough to say whether we want, to keep system around or not.
But I think I'll… Sven, if you make the issue, and I'll comment my perspective, and then… like, the… that same philosophy is where I'm applying, like, in the memory namespace and in the CPU namespace, and in those cases, there genuinely are, like, this scenario where I mentioned, where, like, if you're measuring at an operating system level versus somewhere else, it actually is semantically different.
System.network may not have anything like this, so I'll… I'll comment and explain the perspective, and then you can decide.
**Sven Cowart (ElastiFlow Inc)** 42:45 Cool.
Alright.
Does anyone have anything else?
**Giuseppe Ognibene | Coralogix** 42:51 No, Sven, just let me know if you, like, have any doubts about the issue, or I can do anything.
I just leave it there. I added an event in my calendar, like, in November, and I wanted to talk about the issue, but you… you just did it today.
**Sven Cowart (ElastiFlow Inc)** 43:12 Cool.
Alright, well, thank you guys.
**Braydon Kains (Google LLC)** 43:17 Thanks a lot.
**Giuseppe Ognibene | Coralogix** 43:18 Thank you, bye.
**Braydon Kains (Google LLC)** 43:19 too.
**Giuseppe Ognibene | Coralogix** 43:19 Joy.
**Antonio Martinez (Cisco Systems, Inc.)** 43:20 Thank you.
