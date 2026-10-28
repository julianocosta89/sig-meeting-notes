SIG: Client SIG
Date: 2026-10-27
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Vishwan aranha** 00:38 In March.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 00:42 Hey, Vishwan, how are you?
**Vishwan aranha** 00:45 Pretty good, how about you?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 00:48 Oh, God.
I'm doing okay. It's, not feeling that great today, but I'm doing alright.
**Vishwan aranha** 00:54 Everything okay?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 00:55 Yeah, yeah, no, I'm just, have some allergies, or…
**Vishwan aranha** 00:59 Okay.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 01:00 Yeah.
**Vishwan aranha** 01:02 Hope you feel better soon, take some rest with the weather changing, yeah.
It's becoming colder and colder every day, so…
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 01:11 Exactly.
**Vishwan aranha** 01:15 Hey, Jason.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 01:17 Alright, Jason.
**Jason Plumb** 01:21 How's it going, folks?
**Vishwan aranha** 01:24 Pretty good.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 01:25 It's going.
**Vishwan aranha** 01:27 Seems like you're ready for Halloween with the shining background, so…
**Jason Plumb** 01:32 I am, it's, yeah, it's the best holiday.
**Vishwan aranha** 01:37 Do you like Halloween or Christmas better?
**Jason Plumb** 01:40 Oh, Halloween for sure.
**Vishwan aranha** 01:44 Anything specific about Halloween?
**Jason Plumb** 01:49 I mean, I like to live that every day is Halloween, but I mean, this is, like, the pinnacle day, you know, of all the days you finally get to do it.
Yeah, I like… I mean, fall is my favorite season, I love it.
**Vishwan aranha** 01:59 Yeah.
**Jason Plumb** 02:02 Yeah, I'm…
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 02:05 Hey, Jared.
**Jared Freeze (Palo Alto Networks)** 02:09 Hey, how's it going?
**Vishwan aranha** 02:13 Pretty good, how about you?
**Jason Plumb** 02:18 Give me one of these.
Just since I saw your Dodgers hat.
**Jared Freeze (Palo Alto Networks)** 02:25 Oh… I was like… I don't remember if you were holding something up. I like your Overlook, background.
**Jason Plumb** 02:31 Hey, Alan.
Thank you.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 02:40 Well, it's 3 minutes past. I have a few things on the agenda.
I can go through.
Let me share my screen.
**Ted Young (Raintank, Inc. – Grafana Labs)** 02:50 Let's do it…
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 02:53 Hansen said that he was sick and wouldn't be able to join today.
Alright. So, just one small thing, this… Namespace… The end user namespace is the first one we're migrating.
I've approved it, but per our policy that we agreed on.
One other person needs to approve it, so… maybe Jason or Jared, like, if you have time today or this week sometime, if you could look at this and just give it a stamp.
That would be great, I think.
The, the namespace in the core registry has already been deprecated.
So, and this, this PR points, like, updates the, Let's see… Yeah, the manifest to point, like, to that hash, to that commit hash that has… The deprecation there, so… Yeah, so this, this kind of finishes that first namespace, and we can move on to the next one.
**Jason Plumb** 04:04 I should be able to take a look, hopefully today.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 04:08 Cool, thanks, appreciate it.
Alright, and then… then I have two topics that are related.
I went to the… Core Semantic Conventions meeting yesterday.
And there was a little bit of discussion about the device namespace.
Which… They're trying to… basically, they're in the process of converting all the… all the conventions to the V2, model.
And… I think there was, the device… Had… was listed as an entity.
But it didn't have… Identifying attributes, which in the V2 model are required.
So,
**Jason Plumb** 05:01 Was that… has that always been an entity?
That can't be right.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 05:06 Let's see… Well, they, they, actually, they just changed it. I just saw that PR.
Yeah, this PR, I think, was just merged.
No, not this one.
Oh, hold on.
**Jason Plumb** 05:36 Yeah, this is doing the opposite, this is, like, changing it back to attribute groups.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 05:40 Yes, correct, yeah.
**Jason Plumb** 05:41 Okay.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 05:43 Because… and yeah, so the discussion essentially was that It wasn't clear, like, which attributes should be identifying for device.
Because the device ID is, Sensitive, and it will not always be collected.
So, yeah, I think Ludmila actually changed it back to just, attribute group.
In the core, but when we bring it in, I thought we should have a discussion about this, if you want to model device as an entity or not.
And Browser is kind of in the same, same boat.
A little bit different, but… In that, so… Let's see, Ludmila was… yeah, she was proposing here maybe having a discussion about splitting the device into two?
things. Like, one would be… One entity would be, like, the device model, which is identified by the brand version, or whatever, Kinda identifies just a model thing. Just a device.
Kind?
And then, maybe a separate… optional entity that would have the ID. So, like, if you did have the ID, you could send it as, like, the instance of that device.
**Jason Plumb** 07:04 And you could also imagine a manufacturer.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 07:08 Yeah.
**Jason Plumb** 07:08 Yeah.
I mean, I don't have a pressing need for that, and maybe no one else does, but just in terms of data modeling, I think there's other… Other things, which kind of suggests an entity.
I think we should definitely… I mean, if this is something that came up in the other PR, that's fine, but I think we probably don't need to consider The sensitivity of… components when we're considering the modeling of the data, I think those are two separate concerns.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 07:41 Okay.
So, when we work on moving this here, should we just bring it as first as a… As an attribute group, and then… Someone can propose, you know, how to move that into an entity.
Or two entities.
Yeah.
**Jared Freeze (Palo Alto Networks)** 08:11 I guess… I'm still a little confused. Why would you have two? Why would model and ID be… Separate.
**Jason Plumb** 08:20 I think the model's, like, the Samsung Galaxy S9 or whatever they're on, I don't know, and then the ID was, like, a unique identifier for that instance of a Samsung Galaxy.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 08:30 Yeah.
**Jared Freeze (Palo Alto Networks)** 08:33 Gotcha. Okay, I guess I see. So it's like the grouping, then.
**Jason Plumb** 08:37 Yeah.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 08:42 And browser is an kind of similar thing. Like, we have… We have an entity for… just called browser, but it's really not the instance, it's just… it's like the… Like, the browser name and version, essentially. So, just the kind. And there's no identifying attribute for a browser instance, so I think it always would be just the kind.
Which I think is fine.
**Jason Plumb** 09:11 I wonder what they call it on Android. I'm looking at my phone right now to see if I can find this.
Yeah, there's something called an EID.
On Android. It's probably sensitive, and you don't want to share with people.
Of course, there's also the IMEI stuff, but… Something called an EID.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 09:47 Okay.
Alright, so yeah, I think… I think the next move is just, to migrate it as a group, and then we can go from there.
**Jason Plumb** 10:04 I like it. I'm fine with that.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 10:07 Right, cool.
**Jason Plumb** 10:08 The simple thing, and then make it more complicated as needed.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 10:14 Do you do reports? Do you use an entity right now in the Android SDK?
**Jason Plumb** 10:18 We don't have any entities yet.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 10:20 entities, okay.
**Jason Plumb** 10:21 No, the APIs that we're using don't really support it.
That well yet. I mean, I think Java just merged the API for some entity support, but there's no way to get it surfaced in the resources yet.
Like, via resources.
Soon.
Never been closer.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 10:47 About the browser, very quick, Let's see… so yeah, here's… here's the browser… entity, but I think this is still in… the, the, V1 model?
So it doesn't have identifying… Attributes defined.
I guess, like, If we move it over.
Because we are using, V2 from… from scratch.
We'd have to figure out, like, which one, which of these attributes would be identifying.
**Jason Plumb** 11:29 It's like user agent and nothing else.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 11:32 Well, okay, so user agent… It's a little bit pro… it's not really clear, because user agent is kind of frozen and deprecated.
**Jason Plumb** 11:41 Oh, it is?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 11:42 At this point, yeah, it's, it's like, it's moved to these, other attributes, this, this browser.
**Jason Plumb** 11:48 There's, like, parsed components of the user agent?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 11:51 Yeah.
**Jason Plumb** 11:52 Essentially.
Yeah.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 11:54 But this, this… this brands one is… is… contains multiple ones, like, compatibility… for compatibility reasons, like, it's not just, like, the actual one. I mean, you could… so you can extract, like, the main… The main model from it. Sorry, the main name from it, but it doesn't contain just that.
So… I think if… I think what probably would make sense is to extract extract the, like, the single name and version, and just introduce a new attribute as the identifying attribute, but… Maybe I should create an issue about this, can I describe it in more detail?
**Jason Plumb** 12:55 Yeah, the issue is to, like, what do we do about bringing these over?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 12:58 Yeah, because if you want to preserve it as an entity.
it's not gonna work, I think, the way it is.
**Jason Plumb** 13:04 And it needs… it needs identifying. Okay.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 13:07 Yeah.
Okay, I'll create an issue, purpose.
**Jason Plumb** 13:13 I think that makes a lot of sense.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 13:22 Alrighty.
Do you guys have anything else that you wanted to talk about today?
**Jason Plumb** 13:32 What was, did the release happen?
I know there was talk about a release last time, right?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 13:40 No. I think Hansen said that he was… was gonna do a release, but… I don't think it happened.
**Jason Plumb** 13:47 Okay.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 13:49 And it also seemed like it wasn't as… as… Urgent, because we now… now we're pinning to that commit… commit hash, so…
**Jason Plumb** 13:59 It's certainly not urgent, but I think last time I mentioned that it's nice to get that process started so that we have experience doing releases, so that we can be more regular about it.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 14:09 Yeah.
So when Hanson is back, like, we should… Touch base with him.
**Jason Plumb** 14:14 Okay.
It'd just be nice not to push it out too much farther.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 14:18 Yeah.
**Jason Plumb** 14:21 I'm sure it's gonna sur- I'm sure it's gonna surface some stuff.
**Jared Freeze (Palo Alto Networks)** 14:29 I just had a question. So, the identifying attributes, can you explain that just a little more? I'm not sure what the… request is.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 14:39 So, for an entity, entity needs to have, some identifying attribute or attributes, Which do not change, like, during the lifetime of the entity.
So, like, all your, all your, all your telemetry is, like, Produced from that entity.
Can be tied together and, like, or joined by that… by those identifying attributes.
So I can… in… in the… V2 model, or of the semantic convention spec, like, you need to provide those… what those attributes are.
When you define an entity?
And it is not clear right now what they would be for browser, for the browser entity.
**Jason Plumb** 15:32 And is that a change that happened in V2, or has that always been with entities?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 15:35 Yes, it's new in V2.
**Jason Plumb** 15:37 Okay.
Yeah, I put a link to the resource that kind of describes the goal of that in the spec language.
**Jared Freeze (Palo Alto Networks)** 15:46 Yeah, I saw that. I think… You know, you're working on mobile as well, so we always had the… You know, like, oh, well, user agent is static.
Within a session, that's actually not true.
Like, if you pick up a session after a browser restart.
it's a different user agent. They're like, okay, that doesn't count.
You're like, alright, what about orientation? You're like, well, a desktop is usually a landscape. And you're like, well, not all of them. Windows computers, you can tip on their side. And so it sort of felt like there was nothing that was really the same forever all the time, you know, except for things that we really don't want to track.
which, you know, are fingerprinty sort of stuff, so I think, those conversations were always really interesting, so I'll be… I'll read the docs and stuff to see, but, you know, even things you feel like aren't gonna change, it turns out, might, you know, depending on how you… you know, slice up your experience, so…
**Jason Plumb** 16:48 And we had a conversation way back in the Java days about the number of cores, like, the number of CPU cores allocated to a process, and that can change over the life of a process.
You'd think maybe it couldn't, but it can.
**Jared Freeze (Palo Alto Networks)** 17:04 Yeah, it's interesting. Yeah, the brands thing, too, like he was talking about, Martin said, browser.brands, it's a comma-delimited list.
**Jason Plumb** 17:14 Might want to rethink that, huh?
**Jared Freeze (Palo Alto Networks)** 17:17 It's really… It's really interesting.
**Jason Plumb** 17:20 We have string array types.
**Jared Freeze (Palo Alto Networks)** 17:27 Cool. Well, thanks for the link. Yeah, I'll check this out. I'm still getting up to speed on this. V2 and some of the… You know, more detailed parts of this.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 17:39 Buh- thanks.
Alright, yeah, anything else?
**Jason Plumb** 17:51 I'll go take a look at that PR right now.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 17:53 Cool, sounds good.
**Jason Plumb** 17:55 That's right.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 17:55 See you later.
**Jason Plumb** 17:56 Good.
**Jared Freeze (Palo Alto Networks)** 17:57 dear.
**Jason Plumb** 17:57 Right.
