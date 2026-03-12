SIG: Entities SIG
Date: 2025-12-08
Duration: 37 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth** 00:36 Hey, everybody.
**Daniel Dyla (Dynatrace)** 00:56 Hello?
**krajo** 01:09 Boom.
**Josh Suereth** 01:16 Alright, so sorry, I was just getting, getting so started. Am I not presenting? I'm not.
A bit behind today, sorry.
I also need to… I am limited to just the first 30 minutes today, so apologies, everyone.
I'm gonna have to call it early. So I wanna be a little bit focused, if possible.
Cool, let's do these in reverse order.
Are we okay if we discuss our open PRs?
**Daniel Dyla (Dynatrace)** 01:53 Yep, totally fine. Do I remember correctly that you're gone… Starting on the 13th.
**Josh Suereth** 01:59 It's not the 3rd… I'm gone starting on the 18th.
**Daniel Dyla (Dynatrace)** 02:03 18th, okay, so you'll be here next week.
**Josh Suereth** 02:05 We'll be here next week, yeah, but I… I'm trying to consolidate… like, I will be here for the entity's sake, but I might miss a lot of other stuff, just because I have a bunch to get done before I head out.
Okay, so this is the allow multiple resources in the SDK. I think this is still draft because, I failed to do one thing that I said I was gonna do, didn't I? It was me.
We need… To update the prototypes, to just list our links, that's it.
I think that's the only thing left to get this out of draft, is that correct?
**Daniel Dyla (Dynatrace)** 02:45 Yeah, I have to finish the JS prototype.
Okay.
I didn't really have much time to work on it last week, so I'll… I'll put some focus time on it this week.
**Josh Suereth** 02:58 Yeah, there's a few to-dos that, probably need to do. For the introduction, I might just Gemini this and see if it's not terrible, and throw it in there.
You know.
or, insert your AI of choice, because I don't know… I don't think there's anything that it really is super critical to get right in an introduction. We did have one comment, which is, what should the API SDK do if this is not being followed? So this is, set of entities providing operation must only include one entity per type.
**Daniel Dyla (Dynatrace)** 03:43 I don't understand… what does he mean, what should the API or SDK do if this is not being followed? Like, why would you not follow the specification?
**Josh Suereth** 04:00 This is… so, if a user can define an entity, and the user provides a set of entities that have more than one entity per type to the API, what do you do as an SDK? Like, that's an error.
**Daniel Dyla (Dynatrace)** 04:12 Oh, yeah, gotcha.
**Josh Suereth** 04:13 We're gonna say, like, oh, pick first, pick second, login error. We have a bunch of, like, this is something I don't… I don't think this has to be resolved in the OTEP, I think that can be resolved in the SDK the way we do it in other places.
**Daniel Dyla (Dynatrace)** 04:26 Yep, I agree.
I also think that it's a little bit implied by the merge ordering algorithm and the… Priority order of the entity detectors.
**Josh Suereth** 04:41 Oh, I wasn't sharing the right tab, I'm sorry, guys. Alright.
Yes, I agree that it's implied by that, so, Yeah, basically, if we say that people provide the set of entities in the priority order, then one of them will win. Oh, one sec.
Sorry, I had to take care of something quick.
I'm back, and where were we?
**Daniel Dyla (Dynatrace)** 06:23 I think we were… we had just kind of agreed that this can be left for the spec later, but… It doesn't necessarily need to be resolved in the OTEP and may be implied by what we already have.
But I don't think we need to get into these details in the OTEP.
**Josh Suereth** 06:40 Cool.
Alright, cool, so let's get back to… Just need to shore up to-dos.
We'll get that out for full review then. Next one.
This spec had a bunch of comments on it.
From the entity merge algorithm. I think David Ashpel had a bunch of really good ones.
let's go through, where were they?
Has this came to term Relative Priority of Entities? Everyone asks this, and I think we have this in our OTEP, but not, like.
In this part of the spec, which is, you're gonna define the priority order of an entity by the order of your resource detection.
I don't know if I'm gonna add it into this PR, because I'd like to add it into the PR where we add how we interact with resource detection.
**Daniel Dyla (Dynatrace)** 07:41 Yeah.
**Josh Suereth** 07:43 Okay.
**Daniel Dyla (Dynatrace)** 07:44 Yeah, sorry, I was distracted a little bit. Yes, I think that, it comes from the configuration.
**Josh Suereth** 07:51 Oh, one sec, I left my dog out there. I gotta go get my dog.
Okay, yeah. He was waiting at the door, just kind of saying.
Okay, so next up…
**Daniel Dyla (Dynatrace)** 08:16 I've already replied to this one, but I think, after you loaded the page here.
**Josh Suereth** 08:21 Oh, okay, okay, okay.
**Daniel Dyla (Dynatrace)** 08:23 I had hoped that it would just show up, but I guess it doesn't.
**Josh Suereth** 08:27 Yeah, it depends.
If they're merged.
**Daniel Dyla (Dynatrace)** 08:32 I think it's just the term, like, the phrase ignore, can… implies that you don't do anything, right? So, you're defining the merge algorithm here, and you're describing what the output is. The fact that it's an error condition, you should still log it, I guess, right? It's not.
**Josh Suereth** 08:55 Yes, we should, we should do that. Wait, so we're defining a merge algorithm that, like, won't crash your application.
**Daniel Dyla (Dynatrace)** 09:02 Yeah, that's… you meant it in terms of don't crash. He interpreted it to mean… ignore, which… I guess is the word you used, so…
**Josh Suereth** 09:13 It is the word I use, yeah, so that seems reasonable to update. Like I said, I think David had a bunch of good comments.
**Daniel Dyla (Dynatrace)** 09:18 That's.
**Josh Suereth** 09:19 We had another comment about, this step seems unclear. Does it mean attributes of the new entity can potentially drop attributes from existing E? And then… I just want to cover this one. So basically, there's a clarifying note.
Most readers, for better or worse, are familiar with OTLP data model, than… or OTLP, then the data model document, so they assume the data model equals OTLP.
And we do talk about where entity attributes are encoded as references to resource attributes. We have to cover a scenario about What to do if two entities have conflicting attributes when we encode them in.
**Daniel Dyla (Dynatrace)** 09:59 Agent.
**Josh Suereth** 10:00 Because we can only have one key-value pair.
So… we talked about how we don't want entities to ever share attributes, where an attribute should be owned by only one entity, but in practice, someone could do that. So, need… I need to update the data model to handle that. I think in… my implementation in Java, I was relying on, Protobuff to basically save me from that problem.
And relying on the, like, the distinct notion of how resource works. So basically, the first attribute with that name wins, and the rest get dropped.
But that does mean that, like, one entity's attribute will conflict with another, and one of them wins, and for me, it'd be the highest priority one.
I don't know if that's the right behavior, right? So if we get into a scenario where we have two entity definitions, where they both have an attribute.
And the attribute value is different between the two, for the same key.
What should the behavior be?
**Daniel Dyla (Dynatrace)** 11:08 Yeah, I would expect… the… I would expect the first one to win, because that's been our semantic for everything else.
But… Yeah, so the terminology you have… the attribute is dropped, I wouldn't… You probably want to keep the attribute and resource.
And you want to keep the… Attribute Entity Reference in the first entity.
But remove the entity reference in the second entity?
**Josh Suereth** 11:45 That's kinda what I'm thinking, like… I'm thinking we've had a principle so far of trying to preserve the most amount of data possible.
In this model. So if you end up with a weird conflict, we would say, alright, highest priority entity stays.
Lower priority entity, it's possible we actually have to remove the entire entity ref.
Which is kind of what I'd suggest. So we keep the attributes and resource the exact same to avoid breaking that behavior for people.
The entity ref disappears.
And we kind of convert it to raw attributes, yeah.
**Daniel Dyla (Dynatrace)** 12:24 Then maybe we should add, in other places we have dropped attribute count. Maybe we should add that to the entity.
Just as a signal that something's gone wrong.
**Josh Suereth** 12:34 That's dropped density count, yep, okay.
So, alright, discussion from SIG.
Principle.
Preserve as much… information.
It's possible.
Actually.
Define… Keep highest priority as T.
key conflicts.
T, ref.
Pretty interesting.
**Daniel Dyla (Dynatrace)** 13:15 Are you saying drop the whole entity ref, or are you saying drop just that attribute key?
**Josh Suereth** 13:22 If it's a descriptive attribute key, we could drop it. If it's an identifying attribute key, we have to drop the whole ref.
**Daniel Dyla (Dynatrace)** 13:28 Yeah, so, yeah, I agree.
I would try to keep the entity. If it's a descriptive attribute, I would try to keep the entity if possible.
That's… that's what I was getting at, is, With the… the dropped attribute count.
The entity itself would have a dropped attributes counter.
**Josh Suereth** 13:57 Right, define drop attributes.
Counter.
Entity Ref.
**Daniel Dyla (Dynatrace)** 14:06 And probably dropped entities.
On the whole container, right?
**Josh Suereth** 14:13 Entity jobs.
Yep.
Dropped after it, dropped entities.
on a resource. Yeah.
Yep.
That's in line with what I was thinking as well.
Alright, so we'll put that one there.
That one I thought, was the hardest one to talk through, and I thought was the, like, a really good point. We had not… Actually addressed in the prototypes.
**Daniel Dyla (Dynatrace)** 14:46 And we should probably… Yeah, I guess we'll just log on startup, right, if you have these types of, Conflict…
**Josh Suereth** 14:57 with your normal error logging process that I assume every SDK probably has.
**Daniel Dyla (Dynatrace)** 15:03 Yep.
**Josh Suereth** 15:04 Well, they're required to have it, but that doesn't mean they do.
**Daniel Dyla (Dynatrace)** 15:07 So…
**Josh Suereth** 15:09 Okay, so that's the state of the merge algorithm one.
Cool.
I think… It's weird that it shows the same comment, like, not attached to the… Discussion and attachment.
I hate that. I think it's because.
**Daniel Dyla (Dynatrace)** 15:29 Because he created a review, and then probably added a comment after he submitted his review.
**Josh Suereth** 15:36 Oh, okay.
I still blame GitHub for that.
Alright, and then… so we have, AI is to do in code and on the PR.
The last one is this one here.
Which is the terminology one. I think until Dimitri's able to attend the meeting, I don't know if we're gonna make progress on this besides what we said. I didn't see any response to my last comment.
**Daniel Dyla (Dynatrace)** 16:15 Yeah, I don't think there really has been. Jack's comment is unrelated. He's just saying, if we update it here, we should also update it there.
**Josh Suereth** 16:22 Yeah.
**Daniel Dyla (Dynatrace)** 16:23 If I remember the spec meeting last week… Josh McDonald said he understood why it was confusing, but didn't seem to care very strongly.
you know, didn't seem to think it was a big problem, he just… that it was understandable. I still think I don't even really Understand the problem that's being solved.
**Josh Suereth** 16:50 Yeah. I still think it's basically the way we encode things in OTLP is a little gross, and people don't like it.
And, like, we went through all of the design contortions of what's possible and what… what's gonna lead to the best outcome for OpenTelemetry, and that's where we landed.
So… Yeah.
Alright.
That's it for active work right now, trying to get these things done.
for context, I actually tried to get, I've been toying with Gemini to see how much we can make it do, and what's useful, and I asked it to implement this… the environment variable spec that, Dimitri wrote for propagating entities.
And it actually did a pretty good… oh, and I told it it's not allowed to use only regular expressions, that it had to actually write a parser.
And when I did that last bit, it actually wrote pretty efficient code. It was pretty good. I was happy with it. So, I'm wondering if we can prototype out the, entity detectors that way.
Basically take the spec.
Ask something to write the code, and then go manually clean it up and send it to the, the code owners for review. What do you think?
**Daniel Dyla (Dynatrace)** 18:17 I… I don't know, it depends on… on what it spits out, I guess. I'm trying to decide if I was a… if I was one of the maintainers, would I be… would I find that helpful or not?
**Josh Suereth** 18:31 So, if you give it the right… this one, I… for the Java one, I actually pointed it at the style guide that the JavaSig has. I pointed it at their codebase, and I pointed at the specification, and said, like, follow all of these things. And then I had it spend a bunch of work's money.
Doing that.
So, so, and it did, it did a good job with that caveat. What I found, though, when I went through, a lot of folks have a style guide.
But getting the AI to pay attention to it.
or having the style guide in a way that the AI will use it. With Java, it… It's almost dead simple, where you say, cool, when you're done, run Gradle Spotless Apply, and if it doesn't, you know.
That will fix almost all the style problems.
There's a few other things, like me telling it not to use regular expressions so it didn't end up with this big gunk of hell that was hard to maintain and slow.
That was another one.
But.
**Daniel Dyla (Dynatrace)** 19:40 Yeah, I think it's… it's gonna be more… how do you position it? Like, if you open a PR and say.
like, be clear about the fact that this is generated with AI, and you can either… Modify it, or use it as a prototype, or ignore it.
As long as you… Yeah, I don't know.
I guess it probably will be… it will probably vary SIG to SIG how that would be.
**Josh Suereth** 20:14 How it would be handled, yeah.
**Daniel Dyla (Dynatrace)** 20:15 Because some people are just not going to like the idea, even if the code is great, and all of that. They're just not going to love the idea of AI-generated PRs.
**Josh Suereth** 20:25 Honestly, the number of AI-generated PRs I see in, like, Weaver is already, like… we get more AI-generated stuff than we do human-written stuff, and it's obvious.
So…
**Daniel Dyla (Dynatrace)** 20:41 Yeah, I mean… If it's not a huge lift to just do it and make the prototypes that way, then great.
I don't… I can't… I don't know how the other maintainers would… would receive it. I think I would be fine, but… I know that some people There's a spectrum of how people feel about it.
**Josh Suereth** 21:05 We need to look at the code, and if the code is godawful, don't send it.
**Daniel Dyla (Dynatrace)** 21:11 Yeah, the problem is, I mean, unless I'm misunderstanding what you're saying, you're saying to use it to open a PR for all of the SDKs, right?
So, like, I don't know… Rust well enough, for example, to even say whether it's… like, if I used it to write a Rust PR, I wouldn't even be able to evaluate, like, is this worth sending to them or not?
And, you know, you know Rust, so maybe you would be, but, you know, I don't know, Erlang? Would you… would you be able to say yes or no, this is worth sending to the developers?
**Josh Suereth** 21:48 I can read Erlang, but I cannot, What, what, what's the joke? Like, I, I, I smoked in college, but I never inhaled.
**Daniel Dyla (Dynatrace)** 22:00 You don't care.
**Josh Suereth** 22:01 I don't know if it's good. You know what I mean? So I did the due diligence for the Erlang SIG, it's the TC, so I can read through it, and I can read for, like, does it do what it says it's doing? But I don't know if it's, like, structured well, or that, because I don't have that intuition built in. Yeah.
**Daniel Dyla (Dynatrace)** 22:17 Yeah, I mean, maybe, maybe we should just… offer… rather than creating a PR for every SIG, maybe we should offer, like, hey, would it be helpful for us to make an AI-generated PR for your language, or would you prefer to just do.
**Josh Suereth** 22:32 Yes, true.
**Daniel Dyla (Dynatrace)** 22:32 self.
**Josh Suereth** 22:34 Well, okay, maybe what I'll do is I will show the prompt I used to make the Java one.
Right? So, do it for Java, show the prompt, and then offer the SIGs and say, hey, we think this piece of the spec can be implemented Easily, because it's well constrained, and it has a hard interface.
**Daniel Dyla (Dynatrace)** 22:54 Yeah. So…
**Josh Suereth** 22:55 If you're interested, we'll send you a PR, if not, we won't.
**Daniel Dyla (Dynatrace)** 22:59 Yeah.
I think that's a good way to go about it.
**Josh Suereth** 23:02 Yeah, I don't think we can do this for entity support in general in resource. I tried that as well, it didn't work out so good.
**Daniel Dyla (Dynatrace)** 23:11 Yeah, well, I mean… anything that requires a lot of modification of the SDK. Like, I'm thinking about the prototype that I'm writing in JS right now. It's… I don't… I don't know how AI would handle it.
I can tell you, I've been experimenting more and more to see, like, what it's capable of, and the more context it requires, the worse it gets.
**Josh Suereth** 23:35 limited.
But it can do a really good job if you can train it.
Or you can divide your… if you well architect your components so they're not, you know.
But I ran into an instance where I asked it to do X, and it said, oh, I asked it to, like, match Rust code, Python code with Rust code, and it's like, cool, I can't get the Python code to work, so I'm just gonna go change the Rust code. I was like, no, you're not.
No, that's when we give up.
**Daniel Dyla (Dynatrace)** 24:03 Yeah.
**Josh Suereth** 24:03 Yeah.
It was pretty awesome. Okay.
I got nothing else, by the way. That's it.
**Daniel Dyla (Dynatrace)** 24:13 That's okay, we only have 6 minutes till your drop time anyway, we're missing Dimitri.
And I just need to work on my… prototype. I don't really have anything to show until I do that, so…
**Josh Suereth** 24:28 Dimitri just showed up. I also, wanted to say hi to Creo. I don't know if I said your name right, but welcome.
**krajo** 24:34 Yeah, thank you.
I'm just looking.
**Josh Suereth** 24:38 Okay.
**Dmitrii Anoshin** 24:39 04.
**Josh Suereth** 24:39 You're welcome. If you have any questions, you want to join in, let us know. Sorry, we dove right into details this time, so… That's… Dimitri, welcome!
**Dmitrii Anoshin** 24:48 Yeah.
**Josh Suereth** 24:49 But, maybe it's worth… the rest of y'all can have a discussion. Do you want to talk about this name confusion, PR?
**Dmitrii Anoshin** 25:00 Name Confusion PR. Let's talk about… Oh, I mean, that I submitted some time ago, yeah, yeah, yeah.
I guess I got, approval from you, right? And…
**Josh Suereth** 25:13 I… I rescinded it, actually, after we talked about it.
Although, I don't see my full comment.
**Dmitrii Anoshin** 25:22 Maybe it's not an issue, because there is an issue, and…
**Josh Suereth** 25:26 Oh, I think it is an issue, yeah.
Yeah, here we go.
**Dmitrii Anoshin** 25:54 Okay.
**Josh Suereth** 25:57 Yeah. I… I talked to David Ashpole a bit about just collector PData issues, because, I don't know if you saw what the profiler group is doing with P data, but it's, it's, we're hitting some of the limits of performance and ergonomics. Like, we can either make something that's ergonomic, or we can make something that's performant, but, like, we can't do both. So I understand the complication you have here.
But the, yeah.
And apparently I can't spell correctly, let me fix that.
We want to consistently call it identity that is a set of attributes, and description that is a set of attributes, right?
**Dmitrii Anoshin** 26:42 Okay.
**Josh Suereth** 26:44 But the, like, not using descriptive and identifying when we describe attributes, that's just English.
what… we're trying to understand what the actual confusion is from the, collector side here.
I think we're consistently using, like, we have a thing called an entity ref.
And it has a key which represents a key somewhere else, which is somewhat similar to how profiling dictionaries work. Have you seen the profiling dictionary signal?
**Dmitrii Anoshin** 27:19 I mean, I looked into that, but… I mean, I understand why it's needed for… But I don't know, I don't see the similarity here, essentially.
**Josh Suereth** 27:33 You don't see the similarity between the two, or…
**Dmitrii Anoshin** 27:35 Between the, well, this problem and profiling problem.
**Josh Suereth** 27:40 I think that the naming… the naming problem is what we're getting at. So basically… We have description versus descriptive.
**Dmitrii Anoshin** 27:52 Yep.
**Josh Suereth** 27:52 And basically, the description is the… Data model concept, like a… we have a description.
Right? That is a set of attributes.
If you were to talk about one of the attributes, you'd call it a descriptive attribute.
**Dmitrii Anoshin** 28:09 Okay, I understand now. It's just, for me, it's, I've got… I tried to follow the proto when I, like, generate some documentation on the collector site and everything, and I've got the… at least two comments saying, like, hey, why we use this, like, description here? Why don't we say descriptive attributes, or something like that?
Because there is some, like, discrepancy between Proto, and between the design doc and everything.
**Josh Suereth** 28:41 Yeah.
**Dmitrii Anoshin** 28:41 created this issue, but I guess… so you, you want to say, if we say… if we use attributes, we, we say descriptive attributes, and identifying attributes. If we don't use attributes, we use description and, identity.
**Josh Suereth** 28:58 Yes. Yes.
**Dmitrii Anoshin** 28:59 But that's not what we have in the… in the proto.
So you're saying it's only applicable to attributes, but not to the keys?
**Josh Suereth** 29:09 The… Yeah.
Okay, let's look at the protocol.
**Dmitrii Anoshin** 29:15 So in Rota, we have description keys.
**Josh Suereth** 29:19 Yes, because it's part of the description.
So… This is where I was trying to tie the knot. Is it under Resource? No, I think it's under common entity ref, yeah.
Okay.
So, where's entity ref? Description keys. Descriptive attribute keys… oh, I see, because we use descriptive here.
So what this should say is, the description of the entity, or these are keys… For the attributes that make up the description of the entity.
Right? But the key is found somewhere… the key is a index into a dictionary somewhere else. That's why it's called keys, right? So, we have… a description where we are using an index on keys into a dictionary that it lives somewhere else. The identity… we used ID, and we probably could have called this identity without calling it ID. I'm fine if we call it… if we stop saying identity and we just say ID, That doesn't bother me either, but this is the same thing, where it's the keys that identify the entity, where to construct the identity, you have to use the dictionary.
**Dmitrii Anoshin** 30:43 I understand what you're saying. I'm just a bit confused why we apply one rule… some rules to keys, and other rules to attributes. Isn't that really pretty much similar thing? Like, why… So you're saying that we need to somehow codify that, we need to somehow say what the terminology we use here, right? Like, to avoid… Yeah.
So we'll do.
**Josh Suereth** 31:07 Yeah, yeah.
**Dmitrii Anoshin** 31:08 So, like, glossary would be, identity, description.
Identity key, description key. And then we have identify an attribute, descriptive attribute.
**Josh Suereth** 31:20 I don't actually want it to be identity key or descriptive key. Sorry.
like… When we use the term identity key.
Right, the identity is the full set of key-value pairs.
Identity key in the proto is like a convention to say, I am referring to something in a dictionary. My identity, like, this is how I look up the identity in the dictionary.
So that's the one that I think is weird. Like, the pro… this is the one that's weird.
I'd love if we could basically say I have, an entity that has an identity, a description. An identity is a set of attributes, a description's a set of attributes. If I refer to a specific attribute key-value pair, I can call it an identifying attribute or descriptive attribute. That's fine, because that's just using English.
the key part, I would love if we somehow had a way to talk about it where it's like, this is the key in the attribute array of resource, like, it's a lookup key.
Like, the ID keys is the lookup key for identifying attributes, or the lookup key for the identity, right?
I don't know if I'm saying this right.
**Dmitrii Anoshin** 32:37 Yeah, fantastic.
**Josh Suereth** 32:38 Yeah, go ahead.
**Dmitrii Anoshin** 32:42 Dan, do you want to add something?
**Daniel Dyla (Dynatrace)** 32:46 No, I don't think so, I mean…
**Dmitrii Anoshin** 32:47 I thought you were talking. So, I get it, I get it. I mean, identity keys, but at the same time.
I understand your point, but I would argue that if we talk about set of attributes, set of key-value pairs.
why that set of key-value pairs isn't the same as set of keys. Not, like… for example, we have a… we have some map with set of key-value pairs, which represent identity.
I still don't understand why that particular thing should be called identifying and descriptive in that case.
**Josh Suereth** 33:26 Can you call it an identity key or identifying key? Like, what I don't want people to do is to create a… like, if you want to identify the entity, we want to create hash and equals on an entity object, right?
If hash only looks at the keys, it's wrong.
**Dmitrii Anoshin** 33:42 Yeah, of course.
**Josh Suereth** 33:43 It has to look at the values, right?
**Dmitrii Anoshin** 33:45 Yeah.
**Josh Suereth** 33:47 Okay.
So, that's why I want to avoid the term identity key.
Right? If we do that, we would call it the Identity Key Ref.
Or the identity reference using a key or something, you know, but that… that… that's the one I find dangerous, is calling it identity key or descriptive key. Even though it's physically what we say here, what we say in English, we should, I… I should probably rephrase this.
Just to make sure people understand that this has to get looked up, right?
**Dmitrii Anoshin** 34:31 Okay, so you, you want to keep, Identity keys and description keys, lookups, and with user identity.
and description terminology. But for attributes, we use descriptive and identify.
**Josh Suereth** 34:48 I think your PR was going, like, the other way. If you… what I guess I'm suggesting is that we should be changing this description over the other descriptions, yes?
Like, if you wanted to clarify language, this is where I think the problem is, in the proto.
**Dmitrii Anoshin** 35:07 And how they would change in that case?
**Josh Suereth** 35:12 I would just change this dock here.
Yeah, the hope was that calling this a reference to an entity would make it more obvious what's going on and be less confusing, but I don't know if we achieved that, because we have to treat these wrong, right?
**Dmitrii Anoshin** 35:35 I don't get what specifically has to be changed here, to be honest. Just to, like, Put more emphasis on the… on the fact that these are lookups.
**Josh Suereth** 35:49 Yes.
**Dmitrii Anoshin** 35:50 Because… because the wording seems, like, aligned to what we… what you said.
**Josh Suereth** 35:59 Oh, okay, okay.
I mean, if you… I'm never happy with things I do, so I would always tweak infinitely. So, like, I still think that the English in this thing could get improved. I have to drop, I'm already 6 minutes late. Sorry, guys.
**Dmitrii Anoshin** 36:22 But just to clarify, I think I understand your concern. So, description and identity for keys, and just without any suffix, but for attributes, we still keep using descriptive and identifying attributes, right?
**Josh Suereth** 36:37 Yes.
**Dmitrii Anoshin** 36:38 Okay, okay. I can update that, everything. I don't have a strong opinion, and I think that makes sense.
**Josh Suereth** 36:43 Okay. Yeah, if you… if you need anything else, let me know. Thank you, everybody, and if somebody… if there's anything else you want to talk about, feel free. Sorry, I have to drop. But good to see you.
Great. I'll see y'all next week.
**Daniel Dyla (Dynatrace)** 37:03 I guess that's it.
Have a good one.
