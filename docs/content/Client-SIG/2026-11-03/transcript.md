SIG: Client SIG
Date: 2026-11-03
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Martin Kuba (Raintank, Inc. – Grafana Labs)** 00:42 Bye, guys.
How are you?
**Jared Freeze (Palo Alto Networks)** 00:50 What's up?
**Hanson Ho** 00:51 No…
**Aditya Reddy** 00:54 There you go.
**Hanson Ho** 00:55 Oh, you can't… My video's not working. Great.
I updated my OS, my peripherals stopped working one by one, Sorry, you don't get to see my awesome post-sick face. I'm sure you guys will live.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 01:10 Yeah, that's a bummer.
**Hanson Ho** 01:13 I got it working, and then suddenly, like, my keyboard stopped working, I had to reboot, and I was like, what the fuck? So hopefully my keyboard still works, at least for the duration of this meeting for y'all.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 01:25 Oh, welcome back.
**Hanson Ho** 01:27 Thanks.
**Jared Freeze (Palo Alto Networks)** 01:30 Yeah, after the update, mine takes, like… 5 to 10 seconds to come on the camera, like the regular camera, so…
**Hanson Ho** 01:38 Seriously?
**Jared Freeze (Palo Alto Networks)** 01:40 Only for Zoom.
**Hanson Ho** 01:42 It's, it's on right now, but it, it, it wasn't on. Like, it's not… you're obviously not seeing anything.
But my IT struggles aside, it's not interesting.
Having two browsers that are both Chrome, but have different profiles logged in. That's fun.
Anyway, I digress.
**Jason Plumb (Splunk Inc.)** 02:07 Oh, I know that one. Yeah.
**Hanson Ho** 02:10 Got it.
Oops, I… You guys all at Kukan next week?
**Ted Young (Raintank, Inc. – Grafana Labs)** 02:21 I will be there.
**Hanson Ho** 02:23 Nice.
**Ted Young (Raintank, Inc. – Grafana Labs)** 02:26 Yeah.
Maybe we can have, like, a client-side meetup at some point.
**Hanson Ho** 02:32 I won't be there, but I think Jason is presenting, right?
**Jason Plumb (Splunk Inc.)** 02:37 I'll be there, yeah. Yeah.
Yeah, Ted, do you know if there's, like, a SIG sign-up sheet for the pavilion?
**Ted Young (Raintank, Inc. – Grafana Labs)** 02:52 A SIG sign-up sheet for the pavilion.
**Jason Plumb (Splunk Inc.)** 02:55 Sorry, for the… for the hotel presence at the Project Pavilion.
I think previously we've done, like, sign-ups for different SIGs to have meetings near there or in there.
**Ted Young (Raintank, Inc. – Grafana Labs)** 03:06 Yeah, I have not thought about that.
**Jason Plumb (Splunk Inc.)** 03:10 It might already exist, and we just don't know about it.
**Ted Young (Raintank, Inc. – Grafana Labs)** 03:12 Well, something that's a little different is I don't think we have the observatory this year.
**Jason Plumb (Splunk Inc.)** 03:17 Right.
**Ted Young (Raintank, Inc. – Grafana Labs)** 03:18 So I was kind of thinking maybe we could all just take over the project pavilion and… What I loved about the observatory, besides it being comfy, was, you know, it was a place for us to all hang.
**Jason Plumb (Splunk Inc.)** 03:33 I think everyone loved it. I think there were just a few key complaints about it.
**Ted Young (Raintank, Inc. – Grafana Labs)** 03:37 Oh, no, there… really? I assumed there was just no money There are people…
**Jason Plumb (Splunk Inc.)** 03:42 We'll talk about it later. Oh my god.
**Ted Young (Raintank, Inc. – Grafana Labs)** 03:44 Alright. You can't…
**Hanson Ho** 03:45 I can't see my grin right now. Key complaints, it's hilarious.
**Ted Young (Raintank, Inc. – Grafana Labs)** 03:49 My god. Okay.
I'm trying to put… I'm just… this is all off-topic, but I've been trying to, like, put the wheels on, like, the next, like, Hotel Unplugged, because people really loved that, but it was the same thing. There were some key complaints.
**Jason Plumb (Splunk Inc.)** 04:06 Yeah.
**Ted Young (Raintank, Inc. – Grafana Labs)** 04:07 having to run the money through a vendor, and that, like.
like, the amount of work I'm having to do to make.
**Jason Plumb (Splunk Inc.)** 04:13 Right? Yeah.
**Ted Young (Raintank, Inc. – Grafana Labs)** 04:14 And now, it's like, I'm so mad.
**Hanson Ho** 04:19 Is the money in…
**Ted Young (Raintank, Inc. – Grafana Labs)** 04:19 Orbid elements.
**Hanson Ho** 04:20 small amount.
**Ted Young (Raintank, Inc. – Grafana Labs)** 04:21 Austin and, like, get anyways, fucking… anyways.
**Jason Plumb (Splunk Inc.)** 04:25 It's not a small amount, Hanson.
**Ted Young (Raintank, Inc. – Grafana Labs)** 04:28 Yeah.
**Hanson Ho** 04:30 It's legit, then. Sometimes it's like, anyway, whatever, this is off-topic.
**Ted Young (Raintank, Inc. – Grafana Labs)** 04:33 It's all off-topic, but anyways.
**Jason Plumb (Splunk Inc.)** 04:35 Okay.
**Ted Young (Raintank, Inc. – Grafana Labs)** 04:40 But I will be at KubeCon, so it'd be great to see you all, and maybe we can just, like, take over the project pavilion and just rearrange it into a comfortable place to hang out.
**Jason Plumb (Splunk Inc.)** 04:52 Yeah, yeah, in Amsterdam, there was some, like, lunch seating that was kind of near where the hotel spot was, and that was… that was pretty good, but… Yeah, anyway.
**Ted Young (Raintank, Inc. – Grafana Labs)** 05:07 Bring, like, a roll of carpet with, like, OTEL printed on it, and just, like, roll it out somewhere, and be like…
**Jason Plumb (Splunk Inc.)** 05:13 Like a pop-up canopy or something?
Totally ragtag.
**Ted Young (Raintank, Inc. – Grafana Labs)** 05:18 Yeah.
**Hanson Ho** 05:19 Martin, do you want to present? I… I don't know what my IT situation is like, so…
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 05:24 Yeah, no worries, huh?
Okay, I have one quick thing. Just, this PR.
That, Jason, I think you asked for. It's very small, so when you get a chance.
If you can just, like, stamp it.
It should be pretty, pretty easy that I can merge it.
**Hanson Ho** 05:50 I've… I've, stamped it, or reviewed it.
Looks good.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 05:56 Cool.
And then… We have a couple topics from… from Eddie.
**Aditya Reddy** 06:05 Yeah, that was just to settle on the names, bringing it to this SIG as well.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 06:19 So, I do have some thoughts on… on… on this, And so we can talk about some things here, So, like, for the IMP, it's… it's… so we have… We currently have… Web Vitals instrumentation that collects INP.
So this would add… the attribution… Thanks.
I think… so, you know, those… all these couple things that, like, I can think of here is that… so all of these, I think, come… these names, come from the Web Vitals library.
Including the definitions, and I think that's the case for, like, the… all the other… some of the other attributes that we already collect, so I think I'm okay with that. It's like it not being a standard document anywhere, but just coming from the Web Vitals library, but I just… I wanted to also… See if… what do others think? I think…
**Aditya Reddy** 07:31 Inc.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 07:32 I think some of the… some of these definitions, also, of these are, you know, like, what the format and the calculations come from the Web Vitalist Library, so… I don't know, like, if you want to document that in the conventions, or just say, this… this is what it collects, and it comes from the Web Vitalist Library.
**Aditya Reddy** 08:00 for me.
**Jared Freeze (Palo Alto Networks)** 08:01 Yeah, is there a reason it's on a wild card?
Like, attribution changes over time, like, it changes with minors.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 08:08 Yeah, yeah.
**Jared Freeze (Palo Alto Networks)** 08:09 And so, http has http.something.headers.star.
Now, I realize that is… Set by the user, and this is set by… a vendor, but it's not set by OTEL. So it's kind of this middle ground. I don't know if anyone has thoughts on this.
It's a lot of me.
That's part of the reason… that's the other reason I initially just did raw attribution and shoved it into JSON, is because the 5 keys that are shared across all web vitals are known, static, and all have the same units. The rest of the .attribution.whatever are just kind of… They get… they get added onto pretty quickly, so… the SEMCON would have to roll with Web Vitals, and that just feels like it's gonna get out of sync. Like, it's another thing to keep track of.
as the miners update from a vendor. I don't know what we're calling Google at this point, but, you know, it's just, like, a third party, right? So… I don't know, that's kind of my thought. Again, I understand it's not set by you, which is what the headers… suggest for their wildcard, so I don't know what the intent was.
It's fucking lazy.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 09:36 And maybe it would make sense to look at these kind of individually as we need them. Like, if… Like, I agree with, like, just dumping, like, all of the attribution in the… In the body of the, of the log.
That makes sense, but it's… it is hard to then, work with, right, on the backend. Like, you have to parse it, and… So if there's, like, if there's, like, one, like, if there's some, like, attributes, like, that specifically are useful For analytics in the backend, then maybe we can just work one by one.
And also, like, at the same time, look how stable those are in the library.
**Hanson Ho** 10:22 So this is from, like, an outsider's perspective, because obviously this stuff is changing a lot, and it depends on implementation and vendors, and…
**Jared Freeze (Palo Alto Networks)** 10:29 Very high quality.
**Hanson Ho** 10:30 Yeah, what… what is the downside in, especially in an experiment or dev kind of, stage, just add these, as attributes? Like, is it onerous to, like, an optional? Like, is it… is it too onerous to… to kind of… semi-force people to put them there if it's available, or is it just not stable? Is it just not reliable because the actual value can be different? That is somehow not explicitly expressed in the, in the… the… You know, like, the format can change without us knowing and things like that. Like, what are the… what are the… what are the reasons we don't just make them semantic conventions and say, hey, these are experimental, and work with them however you want?
**Jared Freeze (Palo Alto Networks)** 11:25 Two things. One is that I presume most people will run this through a loop and convert camel case to underscores, which means that you're gonna have keys introduced with minor bumps that don't have a convention, and you may or may not notice.
Like, if you have an alert on your backend that's like, no keys are coming in, then you might notice, but otherwise, people are gonna get… just random keys. Now, if you hard code them.
that is probably what is the, like, the correct thing to do here. But it also means you're not gonna get new keys. Like, you have to stay on top of that as well, as why Web Vitals moves forward. So, it's not that it's impossible, it's just… you know, we're trying to make it this as easy as possible for people, so I just feel like you need a key manager. You need, like, a person keeping an eye on all of this, and making sure that if you do run a loop.
like, you're just gonna automatically get whatever Google decides. So… That's kind of the trade-off. I don't know how others feel about it. Now, in our own web vitals, I mean, we can sort of do that, as long as the person doing Dependabot updates reads through the changelog every single time and doesn't just blindly update.
I mean, that's kind of, you know, I mean, that would be expected of a maintainer anyways for a library.
You know, that I think is so, you know, essential, to the instrumentation, but… I don't know, it's… it's kind of… It's just overhead.
Yeah, I don't know what you guys think.
**Hanson Ho** 13:01 I almost think having, like, a list that is static and you have to manually say, hey, I want to add these. That's almost a feature, not a bug. Like, I don't… I don't think I want, like, hey, my implementation's added a bunch of stuff, and oh, I'm getting a bunch of new instrumentation or new attributes, that are… kind of screwy, or unvetted, or it might contain PII, whatever it is.
So, while it's convenient, I think, at the implementation level, and maybe the instrumentation should have that, the semantic conventions may be… the intention may… we may want to be more explicit.
So… Not to say that to add extra burden, but, you know, we are versioning this stuff, so… you know, we should know at each version what things exist and what things don't exist.
But, you know, again, this is… Outsider's perspective, take it with a grain of salt.
**Aditya Reddy** 14:09 I see we're pretty split here.
**Jared Freeze (Palo Alto Networks)** 14:26 Yeah, I guess the question is… You know, what's the… what's the convention? Like, what… like, I don't want to invent anything new. Like, if the convention is have keys, we should have keys.
you know, if, if we really do think it's, like, HTTP headers, then I think we should have a wild card.
So, it's like, if every other… You know, language is not doing wildcards, we should not start.
**Hanson Ho** 14:58 Is the alternative, like, a blob, then?
**Jared Freeze (Palo Alto Networks)** 15:03 Well, that's what we're doing now, which is… yeah, take attribution, which is unknown and changes over time, and shove it into JSON. The other reason for that is it's very high cardinality.
Which also is kind of like, you know, from my reading of the docs, you know, something you're supposed to avoid.
And, that's… that's not what this data is.
**Hanson Ho** 15:36 So, as an analog, on Android and then mobile, we have, you know, things like crashes. And crashes sometimes, depending on the platform, have different payloads, that are associated with it. And that stuff, is often written by the OS and is fairly opaque, and even difficult to parse. So for us to say everything that's in a crash payload, we create keys for, that's just not feasible. So, at some point, we have to have, like, a blob to basically say, this is kind of messed up, and you can't really aggregate by it because it's a blob.
But, you know, because of all the versions and all the different things that could affect what goes into the blob, we can't really define things.
Is… is your concern more along the lines of.
Of… of that, or is it more along the lines of… there's always keys being added, and that's why I want a wildcard.
Because I think those are a similar… a same solution can handle, kind of, both.
Worries, and it's just… solve… The good, and not have to worry about the bad.
**Jared Freeze (Palo Alto Networks)** 16:55 I'm not.
**Hanson Ho** 17:00 Or am I off my rockers, maybe I'm still.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 17:02 So I'm…
**Hanson Ho** 17:03 ring.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 17:04 I'm thinking so… I mean, isn't it true, though, like, if you wanted to aggregate on something in the backend, then you would want to know what that thing is? Like… You know, it's like having… I mean, I don't really see the difference between a wildcard and putting things in the body as a JSON, in that case.
**Jared Freeze (Palo Alto Networks)** 17:26 Yeah, I mean, you have to think about what we group on here. So, you're gonna group on the page URL and the interaction target.
Right? The interaction target is the… the core of this thing. What did they click on? Or… or… and then, the, interaction type, right? So… You're like, alright, I have a click on a div. That is… that is my index.
And then everything else, you know, is the sort of stuff you need to pull out. So, you know, I mean, maybe we could think about that.
Of, like, that gets… You know, elevated.
Like, those keys get added? I'm not, I'm not sure.
**Aditya Reddy** 18:06 Yeah, true.
**Jared Freeze (Palo Alto Networks)** 18:07 I agree with that, Hanson, yeah.
Sorry, go ahead.
**Aditya Reddy** 18:12 I was just agreeing with you, like, yeah, those are the basic primary ones.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 18:22 Alright, so, I mean, that's… so that it seems like… maybe we just go that route, that maybe we just add the ones that we know for sure that are useful, and the rest just stays in the body as it is right now. And we just can go… Add more things as… As people come at use cases that they need them.
**Jason Plumb (Splunk Inc.)** 18:44 So, if I can summarize to make sure I'm following what the hell you're talking about, web people.
The idea is that we will have a OpenTelemetry opinionated set of… or subset of web vitals that we've then turned into OpenTelemetry's semantic conventions, client-side semantic conventions.
And then there's a mapping that will happen from whatever the source is into these semantic convention attributes, and then whatever's left over would be… Propagated, or could be propagated in the event body.
Is that… am I doing a decent job of summarizing, or am I way off?
Am I following?
**Aditya Reddy** 19:24 Yeah, that's exactly what I thought.
**Jason Plumb (Splunk Inc.)** 19:28 Okay.
**Jared Freeze (Palo Alto Networks)** 19:30 Thank you for considering that.
**Jason Plumb (Splunk Inc.)** 19:31 Because sometimes… sometimes the web stuff gets deep, and I'm not following, but I think… I think I have it.
**Jared Freeze (Palo Alto Networks)** 19:37 One minor detail I might add is that we may want to keep attribution intact, and not do a subtraction of the keys we already included. I understand that's duplicate data, but taking the entire attribution group is the sort of thing that's going to let you know you know, exactly what's coming out of this third party, which is sort of the issue, right? Like, we don't… we don't control the code, so…
**Jason Plumb (Splunk Inc.)** 20:01 Like, the original event, like, just basically copy the original event, that way you also have it, yeah.
**Hanson Ho** 20:06 Yeah, let the blob be a blob and not a manicured blob. It's like, this is where I got the blob from, at least you can trace the progeny, and then you can pluck out stuff, then cool.
**Jason Plumb (Splunk Inc.)** 20:16 Sure, and that, I mean, implementation-specific, that could be configurable, maybe.
Doesn't seem like we need a convention for that.
**Hanson Ho** 20:25 It'll be optional, just drop the bill.
**Jason Plumb (Splunk Inc.)** 20:27 I think, I think, I think… maybe spec'ing at what the default behavior is is good, but I think the override is certainly possible in either direction.
Aditya, is that kind of… is this along the lines of what you were hoping to get out of this?
**Aditya Reddy** 20:42 Yeah, yeah, it's a good start, yeah.
**Jason Plumb (Splunk Inc.)** 20:45 Very cool.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 20:54 Right, and you had a second topic, also.
This one is for the, For the document span, right?
**Aditya Reddy** 21:09 No, this is the related browser.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 21:11 Oh, okay, never mind then, sorry.
Alright, cool.
Sarah, is there anything else that you want to talk about, Eddie?
**Aditya Reddy** 21:22 No, that's it.
**Jared Freeze (Palo Alto Networks)** 21:25 There was one other thing, you had open, was the, the V2, ER?
I think that needs a review. I wasn't sure about the session-ID part.
I'll let somebody else review it, but… it seems sane, I just wasn't sure what to do with it.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 21:46 Which one is that?
**Jared Freeze (Palo Alto Networks)** 21:47 The, append dependency.
The first one.
**Jason Plumb (Splunk Inc.)** 21:53 Yeah, Martin, you still.
**Jared Freeze (Palo Alto Networks)** 21:54 Oh, I guess nobody else did it.
**Jason Plumb (Splunk Inc.)** 21:56 It's been… you just need to remove your block, I think.
**Aditya Reddy** 22:00 Oh yeah, I pushed, and… yeah.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 22:03 Okay, yeah.
Great.
Right?
Anything else?
**Jason Plumb (Splunk Inc.)** 22:20 So… I see that there's a release tag, but there isn't a release.
We talked about that last time, I thought.
Doing overseas.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 22:30 So we did a release, actually.
**Jason Plumb (Splunk Inc.)** 22:32 If you go to releases, there are none.
See, yeah, there's none. So… oh, there is one! What the…
**Aditya Reddy** 22:42 It didn't show.
**Jason Plumb (Splunk Inc.)** 22:44 Weird, okay.
**Hanson Ho** 22:46 It's… it's a pre… it's like a dev, so it's… it's not like…
**Jason Plumb (Splunk Inc.)** 22:49 Oh, it's a pre-release, it hasn't been released yet, that's why it didn't show up. Okay, so it hasn't actually been… Like, is it ready? Like, is this done?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 22:59 Why is it not the race? Like, what?
**Hanson Ho** 23:01 Oh, so…
**Jason Plumb (Splunk Inc.)** 23:03 If you go to edit, you can make it a real release.
**Hanson Ho** 23:07 Yeah, so the idea… the idea is that, the… all the automation creates the draft, but after everything is done, then you're able to, actually push the release. Like, you'll review these notes and things like that, and say, hey, it looks good, and then you press the button manually.
It's, I think… I think it's updated as part of the README, or the releasing, or whatever, If it isn't, then I should push that out.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 23:38 So how does this become an actual release here?
**Jason Plumb (Splunk Inc.)** 23:40 Move it to release label none.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 23:43 Oh, really?
**Hanson Ho** 23:44 Yep.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 23:45 Okay.
**Aditya Reddy** 23:46 Wow, that is so confusing. I know.
**Hanson Ho** 23:48 I thought it was something different. That the UI changed? No, this…
**Jason Plumb (Splunk Inc.)** 23:52 Yeah, it shows up on the main page as a release now.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 23:57 Okay, huh.
**Jason Plumb (Splunk Inc.)** 23:58 That's what I was confused by.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 24:00 My bad, my bad.
**Jason Plumb (Splunk Inc.)** 24:01 No, but now we know, so as part of the releasing, can we check releasing to make sure that that's captured?
**Hanson Ho** 24:07 Est…
**Jason Plumb (Splunk Inc.)** 24:14 Why, pre-releases.
Is that the section there?
**Hanson Ho** 24:18 Yeah.
**Jason Plumb (Splunk Inc.)** 24:19 Yep.
**Hanson Ho** 24:27 Oh, it's been a few weeks since I wrote this, geez.
I thought pre-release is the same as a… actual lease, but for dev, Oh, maybe?
**Jason Plumb (Splunk Inc.)** 24:44 It's weird, the definition is weird, I think it's, like, it's kind of like a… I have always thought of it as, like, a staged release.
It's like, the release is pending, and once we change it, it'll be a real release. So it allows people to see and test stuff without… It being…
**Hanson Ho** 25:02 But the whole Weaver… okay, if that's the case, then I need to… well, I'll take an action item to change this, because the idea is that all dev releases are effectively pre-releases, but they are releases in terms of that you can depend on it. But just… there's a… there's not that assurance guarantee that.
things are in one release is going to be in the next one when it's dev. But structurally, it shouldn't look any different.
We're pre-release.
**Jason Plumb (Splunk Inc.)** 25:32 Sorry, sorry, is V0.1.0-dev, is that sort of the pre-release for 0.1.0?
**Hanson Ho** 25:42 No, 0.1.0, and… so dev is that version that includes everything, and without the dev prefix, it includes only the stable ones. I don't know if there are any stable ones that we have right now. So these are effectively It's one code base, two… views on what exists in the release, and the release is really just the registry, and what attributes are included. So the idea of having dev, is… is so that we could, like, move stuff in and out,
**Jason Plumb (Splunk Inc.)** 26:17 Got it, and we're doing… sorry, we're doing that stupid OpenTelemetry thing where we say development because people are scared of the word experimental.
**Hanson Ho** 26:25 Yeah.
**Jason Plumb (Splunk Inc.)** 26:26 Got it.
**Hanson Ho** 26:26 Yeah, it's, it's… this is, this is Weaver, this is Weaver terminology.
**Jason Plumb (Splunk Inc.)** 26:30 Yeah, okay. That's confusing to me sometimes, but I get it. Okay, so there ought to be, so… do we… do we have anything that's stable yet? Like, will there be a 0.1.0… stable, or what do we call it? Just 0.1.0, or stable?
**Hanson Ho** 26:46 Yeah, just without, without, the dash. I want to say that if we have moved the session stuff in there, the session stuff might be stable?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 26:57 Is… is it?
**Hanson Ho** 26:59 Baby!
Such an IDE probably is.
**Jason Plumb (Splunk Inc.)** 27:08 I'll eat a beer if that's true.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 27:10 Yeah, I don't… no, it's not.
**Hanson Ho** 27:13 Even session ID? God damn it.
**Jason Plumb (Splunk Inc.)** 27:17 Wishful thinking.
**Hanson Ho** 27:18 Fair enough.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 27:19 It's a good question if there's anything client-side related that's actually stable.
**Hanson Ho** 27:24 Well, the reason why I haven't set up infrastructure to release the non-dev version is that if there is one, there aren't that many. So, until we want to release one that is, you know, truly stable, we don't have to kind of go down that direction.
But it… we could, is the thing, so… But I think this is the first release anyway, right? I don't think any other repo has done any releases, so…
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 27:53 Right, yeah.
And Hanson just to clarify, like, the, the non-dev… Releases would start at 1.0.
**Hanson Ho** 28:02 No. The number is, well… we could do that. It doesn't have to. So, these are just, Semver strings, right? So, we could start at whatever number, like… Like, it'd be weird to be… to have 0.1… zero as the, first non, dev release, and that basically pointing to, you know, some tag that is, like, way far in the future. So, I think… what I'm thinking is that the number kind of keeps on going, as we do releases, and then, we just have a dev version and a non-dev version. Once we have a non-dev version, we just have a non-dev version going.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 29:00 That's a bit confusing, but yeah.
**Jason Plumb (Splunk Inc.)** 29:02 Yeah, it kind of diminishes the semantics of Semver, but whatever.
**Hanson Ho** 29:07 the whole dev thing… I know. No, I don't disagree, but that's the way… Weaver has it set up, and…
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 29:18 So when would we move to one boy next time?
**Hanson Ho** 29:24 Good question, anytime we want, and also… when there is a… when there's a marketing reason to do so, maybe? I don't know. Oh, it's 10.30. Maybe this is something we can defer to… to next week, to talk about, hey, what does 1.0 look like?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 29:41 Yep, sounds good.
**Jason Plumb (Splunk Inc.)** 29:43 Alright, front-load the agenda. We'll do it next time.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 29:45 Cool.
**Hanson Ho** 29:46 Knicks.
**Jason Plumb (Splunk Inc.)** 29:47 I'll be in KubeCon next time, so I won't be there.
**Hanson Ho** 29:49 Oh, okay.
**Jason Plumb (Splunk Inc.)** 29:50 Okay, bye.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 29:51 Alright, thanks.
