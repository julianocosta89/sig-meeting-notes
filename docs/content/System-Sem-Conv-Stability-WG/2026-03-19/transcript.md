SIG: System Sem Conv Stability WG
Date: 2026-03-19
Duration: 13 minutes
Zoom Recording URL: https://zoom.us/rec/share/E_QuT7Wd1AVYKkl50h7O0rk6UXsUMNdRs2QkOCOfMyQilLXqAXXkz564qGMAWGox.K5AFpG9iY0pWQ6hT
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 00:57 Hey.
**Donal O'Sullivan** 01:01 Blue.
**Pablo Baeyens** 01:17 Will you be at CubeCon next week?
**Donal O'Sullivan** 01:21 Yeah, I'll, I'll be attending.
You going?
**Pablo Baeyens** 01:26 Yep, yeah, I'm… Donal O'Sullivan 01:29 Cool.
**Pablo Baeyens** 01:31 I… Put something on the calendar for… this group to meet on Wednesday.
So… Thanks.
That'd be cool.
**Donal O'Sullivan** 01:43 For sure.
Hey, guys.
**Dmitrii Anoshin** 01:50 What do you want?
**Christos Markou** 03:00 I have a quick question, topic to discuss.
If we don't have anything else.
**Dmitrii Anoshin** 03:08 Sure, that's it.
**Christos Markou** 03:11 Yeah, it's mostly for you, Dimitri. I remember we… I will send the SPR from the specification, Ripple, and… Yeah, I remember… This one tries to also define How relationships work between entities, right?
And, I wonder if this… Should be a blocker for… Progressing with entities, stabilization, or whatever.
For example, the SPR to create the… The new entity, the process, executable.
I guess we would need to define a relationship between the executable and the actual process.
Or vice versa.
So… What do you think?
**Dmitrii Anoshin** 04:01 I don't think it's a booker. Potentially, whenever we define something, we at least need to mention how… Like, semantically, they relate to each other, the entities?
If we don't have a way to… Could you find that in the semantic conventions.
We still can, like, at least putting the wording in the PR, or somewhere that this is, like, exe… process.
Process instance, or process executable would be some kind of child of a process, or instance of a process.
So, as long as it doesn't affect what we define in the entities, identifying attributes and descriptive other research, I think we should be better.
**Christos Markou** 04:52 Okay, would that be potentially, like, a risk, if we define something with words today?
And… Yeah, for… I think for sure we don't have a way to codify this.
The modeling does not support this today.
And even if we define this within words.
Then if we revisit this and have a way to specify this in a, like… Specific part of the spec, or whatever.
We still might find issues, or we need to change the way that relationships exist.
Yeah, but I'm not sure. I would not be surprised by that.
**Dmitrii Anoshin** 05:36 There is the risk, you're right. I'm just… I just don't want to block, personally, things that I work on block everything else.
**Christos Markou** 05:46 Yeah.
**Dmitrii Anoshin** 05:47 As long as it doesn't seem, like, significant enough. So, for me, there is a risk, yes, but it's not, like, a big risk, I would say, so… I cannot… confidently say that we are blocking, but yeah, you're right, there is some risk. So, if you want, we can expedite whatever they're doing there. If you can review and approve that PR, that would be perfect.
Yeah.
**Christos Markou** 06:13 So, essentially, is there anything, like, any specific reason for not progressing with that?
**Dmitrii Anoshin** 06:19 No, there is no reason. I think, I wanted to… the last thing I wanted to do is to put some examples between.
Hmm.
application… entities, let's say service and infrastructure entities. It's just an example, that's what we… last time we discussed on this entities call. But other than that, it's ready to go, and Josh approved that, so… There is one… another comment, I'll… I'll probably address it today.
**Christos Markou** 06:51 Yeah, I now realize that the service entities are also stable, even without these. So, yeah, there is already some unconventions that are… Ready without, Zeish being there.
Okay, challenge good then. Yeah.
I don't think that we're on a super, like, party situation here, but yeah, let's see.
In any case, I guess this will happen after KubeCon. Oh, we're already there.
**Dmitrii Anoshin** 07:30 Right.
**Christos Markou** 07:35 Okay, yeah, that's what I have.
I guess, I don't know.
**Pablo Baeyens** 07:50 in terms of.
**Christos Markou** 07:51 Beautiful.
**Pablo Baeyens** 07:51 don't know, PR… then that is not a blocker, right? Is that the conclusion?
**Braydon Kains (Google)** 08:03 I think it's not a blocker for a release candidate. Sorry I'm late, if that's what we're talking about.
**Pablo Baeyens** 08:11 No, I was asking about the conversation that Dimitri and Christus were having. Sorry, I'm…
**Braydon Kains (Google)** 08:15 Okay, sorry, I missed the start of that. The gRPC vulnerability blew up my morning, so I was late.
**Pablo Baeyens** 08:24 I'm a bit, of a new guy when it comes to entities, so I… I wanted to double-check that.
**Donal O'Sullivan** 08:42 It was my understanding from the conversation that it won't be a blocker.
Is that right, Chris?
I think…
**Dmitrii Anoshin** 08:50 It's not… As long as we have an idea, at least, of how the relations would be, and maybe… It would be good to put them.
In the docs, at least How do they relate to each other?
**Donal O'Sullivan** 09:10 Okay, cool. Yeah, I can probably… I can update the PR, I guess, and maybe add something along the lines of that somewhere.
**Dmitrii Anoshin** 09:19 Thank you.
**Pablo Baeyens** 09:29 on… so once… I guess after we merged this PR… Should we talk about making a release candidate for the process namespace?
**Christos Markou** 09:51 That's… fine by me.
**Braydon Kains (Google)** 09:53 I think it's fine by me as well.
**Dmitrii Anoshin** 09:56 That's good.
**Pablo Baeyens** 09:57 Cool.
Yeah, I guess off by… by one week or two for GubeCon, but… It's… It's good to be here.
**Braydon Kains (Google)** 10:06 We almost made it.
**Christos Markou** 10:08 Yeah, most of us will be… I… yeah, I guess all of us will be there, so maybe… didn't even happen there.
**Braydon Kains (Google)** 10:14 press the button live on stage, during Roger's talk.
**Pablo Baeyens** 10:24 Okay, and yeah, I mentioned it before, but I put something on the… calendar for meeting next week, on Wednesday.
On Sins… I think all of us will be there, maybe we should cancel this call next week?
**Braydon Kains (Google)** 10:52 Yeah, probably. I won't be there, that's for sure.
I won't be on the call, I mean.
**Dmitrii Anoshin** 10:58 Sounds good.
**Pablo Baeyens** 11:00 Put something on… on the dock.
So… See you on… Sunday, or, like, Next week.
**Braydon Kains (Google)** 11:19 I'll be at the Maintainer Summit on Sunday, so I'll see you all there, probably.
**Christos Markou** 11:23 Yeah, cool. See you there.
**Dmitrii Anoshin** 11:25 Are you, Brandon also traveling to Europe?
**Braydon Kains (Google)** 11:28 I am, yeah.
**Dmitrii Anoshin** 11:29 Oh, nice, we'll be… oh, we'll be there, that's cool.
**Braydon Kains (Google)** 11:31 Yep, all of us will be there. Gonna be good.
**Dmitrii Anoshin** 11:33 Yeah, happy to see you in person.
**Braydon Kains (Google)** 11:35 Yeah, pretty good.
**Christos Markou** 11:36 folks.
See ya. Bye-bye. Thanks, everyone.
**Braydon Kains (Google)** 11:40 Yeah.
**Donal O'Sullivan** 11:40 Hey guys, bye-bye.
