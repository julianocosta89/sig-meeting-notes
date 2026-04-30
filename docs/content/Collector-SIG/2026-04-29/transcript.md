SIG: Collector SIG
Date: 2026-04-29
Duration: 31 minutes
Zoom Recording URL: https://zoom.us/rec/share/D6dVzj_vfZQTLDCMWbd5sdmYbyXlzM5YjY4tQhyexiqs8Mn5k1KYxp4KErPkFriz.oxSAvK0CvhDlhvDV
============================================================

## Zoom Recording Transcript

**Jade Guiton** 04:51 Alright.
Forget started?
**Pablo Baeyens** 05:02 Only one minute.
Yep, so… I added the first topic just… Please review… It's a PR by Evan to… a low… rapid scalar values with config optional, and that's relevant for stabilizing… Some of the configuration, modules.
**Jade Guiton** 05:35 We're sure we want to review it right now? It's still in draft, so I don't know if Evan plans to do… I'll have to do a bit more work order on it or not.
**Pablo Baeyens** 05:46 My understanding from Monday was that he… Well, it's okay, but… I guess, yeah, truly just… That's what it is.
mark us, I… I'll double-check with Evan. I hoped he would be here, but he's not. If he joins later, we can… We can talk about it.
with him.
**Jade Guiton** 06:11 Probably a bit early, right?
Yeah.
**Pablo Baeyens** 06:15 Yeah. Yeah, but it's your own daughter times.
Yeah, you can take a look knowing that it is a drop.
Or it is marked as a drop. But I think it will be marked as very forward review soon.
**Jade Guiton** 06:28 Makes sense.
Are there any other aspects of discussion related to, component stability, any updates?
**Pablo Baeyens** 06:47 Raydon will write something for the… errors, but I don't think it's ready for… a review yet.
I guess if… The topic here is if you're interested.
bring it up with Braden, talking about… Consumer error?
And, yeah, Mikolai?
**Mikołaj Świątek** 07:09 Anna, and can you hear me, by the way?
**Pablo Baeyens** 07:14 Yes.
**Mikołaj Świątek** 07:14 Hello? Okay. So, one thing that came up, and unfortunately came up last week after Dora left, Pablo, was, like, Evan was a little bit confused about the config HTTP discussion, because I guess it wasn't really clear whether the fact that a component is marked stable means that we aren't allowed to change, like, the config X, let's call them. Yeah.
**Pablo Baeyens** 07:46 Yeah, I…
**Mikołaj Świątek** 07:47 Is this, like, written down somewhere?
**Pablo Baeyens** 07:49 I talk about this with Evan, and we will… we will update the… the components ability document to… to document this, because I… I think… I agree it is confusing, and my comment made it more confusing, sorry.
But…
**Mikołaj Świątek** 08:03 No, no, no.
**Pablo Baeyens** 08:03 Generally, what we discussed is, like.
We should be able to change?
Things before the component is… It's Marcus 1.0.
At least what.
**Mikołaj Świątek** 08:15 So…
**Pablo Baeyens** 08:16 the Go API.
**Mikołaj Świątek** 08:18 For the Go API, but not for the YAML struct, is, like, the impression I got from what you were writing in the config.http part, at least.
**Pablo Baeyens** 08:29 That is the position I held before I… We discussed this on… I can see the argument that we say there's no Changes allowed until a major version?
Chains happened, and… You could argue that 0.x to 1.x is a major version change.
In any case, I think it's still too unclear, I think Evan was going to… To update the component stability guidelines.
I'd be interested in if you have an opinion on Pontius.
And what we…
**Mikołaj Świątek** 09:14 Shit.
**Pablo Baeyens** 09:15 Should allow change or not.
**Mikołaj Świątek** 09:17 I mean, my opinion is that… we should… like, if we… if we marked the OTL… let's say the OTLP receiver as stable, then we should avoid breaking changes to its configuration on, you know, Unless they are explicitly marked as unstable. Because this is very possible, right? Profiles are in alpha, if there's something specific to profiles in that configuration, it could change.
Right? And that's, like, I think that's very normal, but there isn't really… in the specific case of config HCP, there is no indication anywhere that any of that is unstable in the component documentation, so I would… I would, Err on the side of, err on the side of stability and just eat the additional maintenance of having to support the older way, like, let's say the keep-alives are configured as well, which is, I think, what you wanted to do as well. I don't know if this is, like, necessarily a policy that is easy to write, because again.
components can have parts, or sections, or features which are unstable, right? This is just something that can exist. As long as they document.
which parts are stable and which parts aren't, I think that's fine. But, like, I think only in that case should we allow any breaking changes, at least to the config struct.
Does that make sense?
**Pablo Baeyens** 10:52 That makes sense, yes. Yeah, that makes sense.
I don't… I wish we had Evan here, I guess is what I'm saying, but that makes sense, and that aligns with my… what my position has been in general.
the… the only argument I heard against was, yeah, that… going from 0.X to 1.X could be considered a major version change, but, like, users are going to be broken.
Even if…
**Mikołaj Świątek** 11:25 Like, realistically, I… Yeah, I think realistically, this is also a problem, because the OTLP… like, the OTLP components just shouldn't have gone to V1 while configure HCP wasn't. I think that's, like, the core of that.
**Pablo Baeyens** 11:42 They shouldn't have been marked as stable. Yes, yeah. The marking as stable of the OTLP components was before we even had component stability guidelines at all, so, yeah.
**Mikołaj Świątek** 11:56 Yeah, so for configHCP specifically, I'm gonna more or less reapply, apply the change that you originally wanted to apply to it, which is that, the struct changes, and that's fine. The YAML doesn't… the actual config format doesn't change, because we're avoiding breaking changes, and the components might stable, which is unfortunate, but, like, this is something we messed up, so we shouldn't externalize that screw-up to users, I think.
**Pablo Baeyens** 12:24 Okay, makes sense. I will… probably ping Evan and you on Slack to make sure that… We are all on the same page, but that makes sense to me.
**Mikołaj Świątek** 12:50 I think I interrupted you, Jad, sorry.
**Pablo Baeyens** 12:57 I don't remember what I was saying.
Oh, yeah, that, Raydon is working on… Consumer error… Partial success representation.
If you're interested on that topic, please talk to Braden.
That's… There will be an RFC at some point, but we are still not at that stage.
Don't know if there is any other topics for stability?
If not, we can move to the one about… Botching.
**Ravishankar Gnanaprakasam** 13:59 Yeah, I mean, like, I posted that comment, like, you know, we wanted to… we were checking to move from, you know, duplicate the batch process for the reliability issues and things.
So, It was each… earlier it was having to write a big chunk, and now we have to write for each, requests that we receive, so… Is it that thoughtful trade-off that was discussed earlier? I'm not sure, so wanted to discuss on the scene.
**Jade Guiton** 14:42 You cut out for a minute there, but if I understand correctly, the gist of your comment is that You're scared about the… not scared, but worried about the… increase… to… Well, not really an increase, but… Having to do… more disk writes when using the persistent queue.
Because batching is done after… After the queue?
**Ravishankar Gnanaprakasam** 15:12 Yep, yep, right.
**Jade Guiton** 15:14 Hmm.
**Ravishankar Gnanaprakasam** 15:16 Because earlier, we had the batch processor, right? So, which was kind of doing the batching, and then… it would have probably sent it a single request, and the exporter would… I mean, the persistent queue would have done it in a single write.
**Jade Guiton** 15:35 Hmm, that's a good point.
Out of curiosity.
**Pablo Baeyens** 15:41 Have you… have you done any benchmarking of this, or is this just, a supposition?
Not sure.
**Ravishankar Gnanaprakasam** 15:59 Me.
This guy who, I'm not sure, because the host metrics that I try to configure is not giving me the IVO with respect to the process. It's giving me the whole as a system, and I'm not able to draw a conclusion on top of that.
So…
**Jade Guiton** 16:20 There's also the problem that, in principle, it should be the same amount of I.O. in terms of bytes written, it's just batched differently.
**Ravishankar Gnanaprakasam** 16:30 Okay.
**Jade Guiton** 16:32 So, yeah, I guess… I think… I don't think they should block, you know, introducing the exporter helper in components, which seems to be the topic of the issue.
But, yeah, there are definitely some questions about how to make the exporter helper batching more efficient.
One proposal could be to… Like you suggested, have an option to Have batching happen up front.
Not sure exactly how that would work, but… Either up front or inside the queue.
I guess that couldn't happen, that couldn't work for persistent queues, though.
But yeah, another option would be to simply say that this is, an additional… data point, I guess, we… If we… if you manage to make a benchmark that demonstrates this is a significant problem, it could be an additional data point for the need for the… As a new batch processor, slash pipeline processor, slash, however we want to call it.
**Ravishankar Gnanaprakasam** 17:38 Right?
**Jade Guiton** 17:38 It's gonna be another piece of evidence that we do, in fact, need the ability to do batching.
Before the Explorer.
So, yeah, I think… I guess it could be useful to bring that up to… to Josh, maybe?
What do you think, Bubble?
**Pablo Baeyens** 18:00 Yeah, I think that would make sense.
on Dimitri, probably.
**Ravishankar Gnanaprakasam** 18:07 process level.
**Pablo Baeyens** 18:08 review.
**Ravishankar Gnanaprakasam** 18:09 that's where I was stuck, over the last week.
**Jade Guiton** 18:14 Hmm. I mean, I think… I don't know if Mike is cutting out, but I think we only heard part of that sentence.
But, I mean, what's important here is not really measuring the amount of I.O. that's done, because it's presumably not very different.
It would be more interesting to look at the latency, essentially, the actual… Time that it takes to process.
Because if you're writing the same number of bytes, but in smaller batches.
It's definitely gonna be less efficient, but yeah, we want to quantify how much Less efficient it is.
Potentially an option… yeah, thinking about it, if the… the problem is just the I.O, maybe the… maybe this could be something in the sending queue as well, right? Where this is something that databases do, where even if you have multiple transactions coming in that you want to persist. You wait some amount of time before persisting, which kind of delays every transaction, but it means you can write a bigger batch, so there could be… there could be some, like, disk-level batching in the persistent queue specifically. That could be an interesting feature to suggest, and I think that would solve the problem Without changing the mechanics of the exporter helper too much.
Basically, the idea is that we… you… the exporter helper persistent queue would wait.
Some amount of time before acknowledging… A batch.
before syncing to the disk, that way you… you can make a… you can have a bigger batch, I guess.
But yeah, I think the best option here would be to ask Dimitri, or… I guess in this case, it would be Dimitri to ask for input on this.
**Pablo Baeyens** 20:20 Feel free to ping him on AutoCollectorDev, on a thread, and we can talk about it there.
He's… it's unfortunately too early for him for this particular meeting.
**Ravishankar Gnanaprakasam** 20:37 Holden, yep.
I'll try to join the… Sync with symmetry. Meanwhile, we'll try to get some benchmarking on the scene.
**Jade Guiton** 20:50 Thank you, that'd be great.
Move on to Nikolai's point, then.
**Mikołaj Świątek** 21:03 Right. So, there's an issue to… add a new interface for storage clients, and the use case, I think, is perfectly valid and can probably be implemented for existing storage extensions. It essentially allows the ability to iterate over all the keys in a single transaction.
Which is, reasonable and not hard to implement. I'm more asking about Let's say you want to do something like this. What should the… actual rollout look like? How do we modify the interfaces in such a way that it, like, eventually, this isn't something that components have to, exceptionally care about, but also so we don't just… add something to the new… to the interface and force all the storage extensions suddenly to implement that, or just not implement the interface at all. That was, something I was wondering.
Essentially, how do we… how do we, add more requirements to, like, the storage client interface in a way where it's, like, reasonably usable, but also doesn't cause a bunch of breakage?
Downstream.
**Jade Guiton** 22:55 Yes, I have much context on the… So we're just extensions, honestly.
I don't know who would be the best person to talk to about this.
**Mikołaj Świątek** 23:04 It's technically me, because I'm the co-donor.
That's the problem here, see?
We don't have to… we don't have to prosecute this right now, if anyone has, like, an idea of how to do this, because… okay, so I… let me tell you this. Let me explain this. Maybe… maybe that will help a little bit. So, there is the notion of a storage extension.
And a storage extension has a single method, it returns a storage client, and the storage client, fulfills a certain interface.
About how you can interact with the storage, okay? And now we would like to have… extend that interface. We would like to have our storages to do more things than they can do right now. And the question is how to actually accomplish that in, like, a reasonably… ergonomic way. So, the proposal in the issue is pretty much define a new interface, which is called extended client in there, and then anytime, like.
An extension can choose to implement this or not, and then every time a component wants to use that extended interface, it casts the client that gets into that interface, whether it, you know, it succeeds or not, and if it succeeds.
it's fine.
And this is something that works, but it's quite… fiddly.
to do, and it's, like, pushing… pushing this decision to any component that wants to use this. But at the end of the day, I think we will want all of the storage extensions to actually implement this, and eventually move that into the… into the normal interface. So, I'm basically wondering about the… the rollout of this, let's say, how to… how to go about changing those. Because, like, changing the existing interface is, like, is a break and change, right?
Like, anybody who actually fulfilled that interface doesn't fulfill it anymore.
Does that make sense?
**Jade Guiton** 25:12 Yeah, I think it wouldn't be unreasonable to keep it as a separate interface. This is something that we do in other places, too, right? Extensions, in general, are based on the whole concept of You know, you cast to an interface and it may or may not match.
so I guess the bigger the question is, like.
Can we… can you think of a use case to, like… a storage extension that's dealing with an API where you can't do this kind of thing.
In which case, they wouldn't be able to properly implemented. Do you think there would be… A possibility, in which case it would make sense to keep it as a separate interface.
**Mikołaj Świątek** 25:51 Do you think he would…
**Jade Guiton** 25:53 I don't…
**Mikołaj Świątek** 25:54 I'm genuinely not sure. I'm genuinely not sure. I think all of the current storage extensions that we have, and the ones that I know of, can implement this.
Yeah, it's… because we already require transactionality.
By value of the interface, and that's base… and that's, in a sense, that's a wrapper. So, in… in a way, even just being able to to list all the keys in the storage would be enough, because we don't even allow that to happen right now. And the interface proposed in the issue is more general. It basically allows you to do a arbitrary range over the keys in a single transaction. I think that's also implementable everywhere, but I'm also, you know, I don't know what storage extensions exist in the wild, and I'm also wondering what happens if we want to change this interface in the future again. Are we gonna do another extended 2? Or should there be some kind of holistic capabilities-based, setup in there. Because there's also a question of… You have a storage extension, you don't really know whether it implements the new interface or not. How do you know, as a user, whether this is gonna work? If you have a component that needs the new interface.
how does that component communicate this to users? How do users know which extension to use? Like, do we… is there a way for us to catch it… catch this before the component tries to start and look at the extension and discovers that it doesn't implement what it needs? Like, these are the kind of things I'm wondering about here.
**Jade Guiton** 27:34 Yeah, I think this is a… this is kind of a general question about…
**Mikołaj Świątek** 27:39 Yeah.
**Jade Guiton** 27:39 documenting extensions, right? I think extensions in general should specify exactly What interface and what version of an interface?
The… and which interfaces, if multiple, they fulfill.
in the documentation, that way. And also, components should, you know, specify what interfaces they rely on.
So that way you can kind of check compatibility ahead of time, but it is a bit difficult.
Would this be a good place to apply the… The RFC that went… I think that got merged recently… was it merged? I don't remember.
About the functional… interface thing… I'm gonna try and find it.
**Pablo Baeyens** 28:24 I think it did get merged.
**Jade Guiton** 28:29 Component interfaces, is that the one?
Yeah.
I guess it doesn't really… It does help a bit, I'll put the link in the Zoom chat, but…
**Mikołaj Świątek** 28:42 Oops.
**Jade Guiton** 28:44 It helps a little bit with extension, in the sense that you can provide a default implementation.
Which can just be, like, a panic or something.
For the method, and that way you don't necessarily have a breaking change at the interface level.
But, you know, if that's not what the storage… interface uses, you would need a breaking change to implement this pattern in the first place.
**Mikołaj Świątek** 29:17 Alright, I'm gonna… this sounds like a bigger problem in general. Like, if we're okay with doing the casting, and for the record, the cast wouldn't necessarily be of the extension itself, it would be of the client that it returns.
At the end of the day. But this is alright.
Then… I think what is proposed in that issue is okay. If anybody has feelings about this, you know, feel free to comment on it. The proposal is basically just to add the interface, so it's in the storage package, and then, you know, you can start having extensions actually implemented.
And then components actually try and use it.
**Pablo Baeyens** 30:07 The casting sounds reasonable to me. I don't have a strong opinion about the interface itself.
I trust the code owner, being you.
Good.
**Mikołaj Świątek** 30:19 Careful, careful, careful, careful. I am not sure if it makes sense, that's why I'm… that's why I'm bringing it up. I'll ask also the issue, offer some questions about how they imagine this being used exactly, to make clear, at least in the issue, what we think This is gonna look like once it goes out into the wild.
Well, also, market is experimental to start with. So, just… just for good measure.
Alright, thanks, that's all I had.
**Jade Guiton** 30:52 Yeah, and I think, yeah, if there's a worry about breaking changes.
to the interface. Maybe that's a good opportunity to… do a braking change anyway to implement the pattern in the RFC to make, later changes a little bit, Less invasive, I guess.
**Mikołaj Świątek** 31:12 That's also fair. I'll look into it, thanks.
**Jade Guiton** 31:24 Alright, we're at the end of the current agenda, I believe.
Are there any other impromptu topics someone would want to discuss?
Kind of like a no, so… I guess that's it for today. Thank you, everyone.
**Mikołaj Świątek** 31:53 Thank you. Nice to see you.
