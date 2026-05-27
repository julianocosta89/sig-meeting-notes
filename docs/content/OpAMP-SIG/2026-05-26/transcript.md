SIG: OpAMP SIG
Date: 2026-05-26
Duration: 43 minutes
Zoom Recording URL: https://zoom.us/rec/share/33VXhHm1ceNmLqu6XumJuO_FXsMjRozoK4p-4Ur1RW7QeC-L0djfV4Q8voYyuA1E.xuYHJ_mFTg8Xod8D
============================================================

## Zoom Recording Transcript

**Tigran Najaryan** 02:26 Can anyone hear me?
**JM Juande Manjon** 02:28 Yes?
**Tigran Najaryan** 02:30 Works now, okay. Hello.
Alright.
Let's start.
The first one, is Jane here?
No, Jade is not here.
Maybe let's move it to a bit later.
Yeah, restructure folders… From the here? Yes. Yes, I'm.
**JM Juande Manjon** 04:15 here.
**Tigran Najaryan** 04:15 Yeah, go ahead, please.
**JM Juande Manjon** 04:17 So, there recently was a change in the proto package.
adding dot V1 at the end, and this opened the door to have, in the future, V2.
So I was looking at the current proto, structure directory, and it looks like it doesn't honor or doesn't follow the best practices when you have versioning, where when the versioning, you have to have different folders, V1, V2, per version. So, basically, it's just moving the current protofiles to a new structure when you have V1 as part of the path.
This is the more common practice for to follow with protoversioning.
**Tigran Najaryan** 05:07 I think it makes sense to me what you're saying. It will change the directory structure in the generated files as well.
And… I think it may…
**JM Juande Manjon** 05:18 maintained.
**Tigran Najaryan** 05:19 bizarre.
**JM Juande Manjon** 05:19 the proto-content. The proto is gonna stay the same thing.
The only thing that having this, it opened the door in the future to… to scale with new versioning without affecting the… The…
**Tigran Najaryan** 05:32 No, I get it, I get it. What I'm saying is that the import paths are going to change for everyone who is using the generated products.
Which is…
**JM Juande Manjon** 05:42 Right, so…
**Tigran Najaryan** 05:43 Probably okay, I guess.
**JM Juande Manjon** 05:44 So, as part of the submission, I have a branch, both in Open and SPEC, where the Go Opan is consuming the suit model with the new location, and everything's working fine. As well, I added a LinkedIn CI, where we can link Changes in the future. And also, it's integrated with the braking changes as well, using, bus build.
To… to also to… to integrate and highlight any breaking changes in the future.
**Tigran Najaryan** 06:24 Yeah, I think that would be very useful. So, I think I agree with the… with the idea that this is the right thing to do.
But I would like to understand right through… what exactly are we breaking here? Is it just a simple change in the import paths? It is still breaking for all pump go, right?
You said you have a draft of implementation in Go as well?
**JM Juande Manjon** 06:51 I have a branch, it's pointing there in the PR, or in the issue. What I'm saying, if we modify both, they'll pan the GOPA and the spec at the same time, there won't be any breaking changes.
**Tigran Najaryan** 07:07 If you have the, I guess, draft implementations, can you maybe link them here, so that we can take a more detailed look at it?
**JM Juande Manjon** 07:14 Can you repeat again?
**Tigran Najaryan** 07:16 You said you have a draft, right? Can you create, like, draft pool requests, actual.
**JM Juande Manjon** 07:20 Oh, yes, yes.
**Tigran Najaryan** 07:21 And link them from here? You said you have a branch.
**JM Juande Manjon** 07:24 Yes, did you follow to the breaking change of the button to 13.
**Tigran Najaryan** 07:30 This one?
**JM Juande Manjon** 07:31 Yes, and on the bottom, I have a link to… to that branch, but I will… I will do a proper, PR submission.
**Tigran Najaryan** 07:41 Yeah, please create, yeah, create a draft PR, let's take a look at it, and also, you said you have the same thing for OpumpGo as well.
**JM Juande Manjon** 07:49 Yes.
**Tigran Najaryan** 07:49 Right?
Yeah, if you have that already, just write a draft PR so that we can take a closer look at it.
**JM Juande Manjon** 07:55 Okay, indicate I need two PR, because they have different repos.
**Tigran Najaryan** 07:58 Yeah, yeah, yeah, yeah, two PRs.
**JM Juande Manjon** 08:02 And last thing, moving on, so I'm… so I'm… I would like to understand why we have the proto keyword in the package, because for me, that open, proto-V1, that proto keyword doesn't… Doesn't give anything.
So I wanted to understand why it's there.
**Tigran Najaryan** 08:22 What do we have there? Sorry.
**JM Juande Manjon** 08:26 is opan.proto.v1.
So, I think that proto-keyword in the Pakistan is not needed.
But this is a breaking genius.
Did you say light?
**Tigran Najaryan** 08:40 This part, you mean?
**JM Juande Manjon** 08:42 Yeah, doesn't provide anything.
meaningful.
**Tigran Najaryan** 08:53 I guess you're right, and if we're making the change, if we're breaking it, maybe we do it once, maybe we get rid of that as well.
**JM Juande Manjon** 09:01 I mean… If you agree, I will be happy to remove it as part of the PR, but I want to have consensus on that.
**Tigran Najaryan** 09:16 I am inclined to agree to that, yes. I think it would be the right thing to do. If we're doing the breaking change, let's do it at once. Like, let's do it… all the fixes that we want to do there in the path names, paths and the package names.
**JM Juande Manjon** 09:29 Okay, I will take care, we'll send a PR, and we can discuss next meeting.
**Tigran Najaryan** 09:33 Yeah, yeah, let's… let's see the drafts, let's have a more detailed discussion on the PRs.
**JM Juande Manjon** 09:38 Alright.
**Tigran Najaryan** 09:42 Okay, thank you.
**JM Juande Manjon** 09:43 Sure.
**Tigran Najaryan** 09:47 Is, is Jade here now? Yes.
Jade, do you want to go ahead with… For the swamp.
**Jade Guiton** 09:53 Yes, sorry, I was on the wrong Zoom link.
So this GitHub issue I filed regarding the op-amp, agent description.
Identifying attributes part of the payload.
Which, my understanding from reading the spec is that it's, supposed to be a subset of the resource attributes.
that… Are used by the collector itself for its own telemetry.
And I previously filed a PR to help make that match a bit better.
For the service instance ID, but there is still a remaining case where it doesn't quite match.
Which is, when you disable… service.name, service.version, or service.instanceID in the collector's telemetry.
When you do that, the op-amp extension provides defaults for them.
Based on… The collector distribution name version, and I don't remember the default for service instance ID.
But yeah, it provides defaults, which means that… If you are trying to filter the collector telemetry.
By the attributes that end up in identifying attributes, you will not actually find the collector's telemetry.
Which I find to be a bit of a problem.
There was some discussion already on the issue, and it seems it was agreed that it would make sense To, to just put all of the collector resource attributes Under identifying attributes, or at least… A subset of them.
But that begs the question of… I had two questions that were kind of left unanswered previously, which were, The include Resource Attributes, Option, what should we do about it in the DDog extension?
I'm not sure exactly… What the idea is for it, and I guess… there's… I guess both of my questions related to the distinction between identifying attributes and non-identifying attributes.
What is the intent?
of the two of them, right? Because my interpretation would be that maybe identifying attributes would contain the actual resource attributes of the collector telemetry, and then non-identifying attributes can contain anything else that the op-amp extension wants to supply?
In which case, maybe the default values that the authentic extension is supplying Should we move to non-identifying?
And there's also the question of… conflicts? What if there is… What if, for instance, the collector's telemetry contains, os.type?
And that would be put into identifying attributes, but then.
the web app extension would supply its own value in non-identifying attributes.
is that okay? What if the values don't match? The spec is a bit silent on this regard, so I wanted to ask the group What… should we do about this? It's not that big of a deal, but… Yeah, what should we do about this in a way that respects the spirit of this deck, I guess?
Does that make sense?
**Tigran Najaryan** 13:38 Yeah, yeah. Okay, so I guess, first of all, yes, the purpose is that, right? So that… you have two, supposedly two different backends where this data goes to. The agent management system has its own backend, likely.
where the identifying attributes of Open Protocol end up, and there's some sort of a telemetry backend where the collector sends its its own telemetry too, and you probably want to be able to have some sort of a connection between the two, so that if I see an agent on my agent management system, I'm probably interested in seeing the telemetry of that agent elsewhere in the telemetry backend as well. So this is… this is the goal, essentially.
for that to be possible, you want the values too much somehow, right? That's the… that's the purpose of it.
What I do not quite understand here is.
Why would anyone do this? What is the use case for that?
And without understanding the use case, it's a bit difficult for me to… to understand why… why is this even… So, someone… I would say this is… This is a broken state for a configuration for the collector.
**Jade Guiton** 14:50 I agree that this is pretty weird, honestly.
**Tigran Najaryan** 14:53 Why? Why would anyone do this, right? So if they do this.
to, I guess, how much do we want to try to behave in a… in a… I don't know what is the expectation in this situation, right? We could do exactly that. We could take these values.
And put them as identifying attributes if they are overridden this way.
Technically, so we could try to be, I guess, pedantic, and follow whatever the values are here. We'll put the same values in the OPAM protocol as well.
Is there any, like, value in doing that? Maybe, who knows if there is a real use case where somebody needs to do this?
the, like, what do you end up with is essentially nothing in the… in the telemetry? What is… what is the reported telemetry here? I don't know.
**Jade Guiton** 15:52 I agree that disabling all three attributes is definitely broken, especially if you don't replace them by something else.
I can think of some use cases in the steps to reproduce here. I added a separate my service ID attribute, so potentially someone might want To use a completely different attribute key to represent their service.
instead of the standard ones. It's a bit weird, but why not? Or maybe… they only want to disable service.instance.id, because they have issues with, what's it called? Cardinality of metrics, for instance.
I agree that they're not very convincing use cases, but yeah, I do think it's possible for someone to… Encounter that.
I think that in the case where everything is disabled, and you can't tell collectors apart.
That is definitely… a problem, but it's not a… I don't think it's a problem Alpam needs to solve,
**Tigran Najaryan** 16:54 Exactly, I agree with that. The stated goal here is that it should be possible to identify, but if you disable everything that can help that identification, then there's nothing much we can do here, right? I don't know if we even need to try to do anything special in this situation. So, in my opinion, when there's reasonable values here, the user did some overrides, they want a different service name, sure, we'll use that.
And I think your PR does exactly that, right?
And in my mind, I think that's probably the extent of how much we should try to… to be a good citizen here for… for the user.
I don't think situations like this require some extraordinary efforts from our end, and I don't even know what we can do here, possibly. There's probably nothing that we can do if… if they do this.
**Jade Guiton** 17:47 I mean…
**Tigran Najaryan** 17:48 Maybe, I guess, if they start supplying their own complete different set of attributes, then we could use that.
I guess, maybe.
**Jade Guiton** 18:00 Yes, I don't think that's…
**Tigran Najaryan** 18:01 That's necessary, yeah.
**Jade Guiton** 18:03 Yeah, I think that's the main… the main use case here, where someone is… Using the different attribute key instead of just overriding the value.
I guess…
**Tigran Najaryan** 18:15 This is the, I guess, the downside of having too much configurability, in a way, right? So there's the happy path, you stay in that happy path, it works, you start doing weird things, and things will break.
Yes, definitely. We don't know if there's a way to prevent all possible ways For the user to shoot themselves in the foot here.
**Jade Guiton** 18:39 Yeah, and I don't think… I don't think we need to… to do that. My suggestion is just to… I guess… Remove the fullbacks.
That we have for these extremely weird cases.
Because that makes the behavior match what's expected more.
**Tigran Najaryan** 18:56 Yeah.
**Jade Guiton** 18:57 So it's not really…
**Tigran Najaryan** 18:58 Let's say… so you're saying if they disable, for example, just the version, it will be disabled in OPAMP as well, but the rest may be still there. The name and the instance ID are there, and that's enough to identify the agent.
I think I agree with that. We could do that, maybe. I don't know why do we have the fallbacks there, to be honest, so maybe… maybe we do that. That's okay.
**Jade Guiton** 19:21 Okay, yeah.
And, yeah, I guess… The question that was kind of unresolved was… Do we care about… Conflict between identifying attributes and non-identifying attributes?
**Tigran Najaryan** 19:42 conflicts in what sense? Like, the same attribute being in two places, you mean?
**Jade Guiton** 19:46 Yes. So, for instance, if we decide that the identifying attributes should just be the collector's resource attributes with no changes.
Then it's possible that… a user supplies a value for host.name, and this doesn't match with the host.name detected by the op-amp extension and set in the non-identifying attributes.
**Tigran Najaryan** 20:16 I guess…
**Jade Guiton** 20:16 We're doing VR more.
Through these oriented.
**Tigran Najaryan** 20:20 It shouldn't happen, so there's an expectation that there's no overlap between the attributes, between identifying and non-identifying attributes. We could add that to the spec.
It probably was implied.
I think it's not in the spec anywhere, but… I don't see why it needs to be a possibility there, where you somehow have them in both places.
**Jade Guiton** 20:48 Yeah.
**Tigran Najaryan** 20:48 So we can add that, we can say that in the spec explicitly, that It's not allowed.
And then we can enforce it in the implementation, so that if it's already in the identifying attributes, we don't allow it in the non-identifying ones.
**Jade Guiton** 21:06 Hmm. Alright.
Okay, and I guess my remaining question was about the include resource attributes option. I don't know if this is used by the… up-amp supervisor, or something like that.
**Tigran Najaryan** 21:20 Is it an extension configuration option?
**Jade Guiton** 21:23 Yes.
**Tigran Najaryan** 21:23 Is that in the extension?
**Jade Guiton** 21:26 Yes, it's an extension config option that seems to put all of the resource attributes from the collector into non-identifying attributes.
**Kelsey Ma** 21:36 I actually opened an issue on the supervisor to include configurability for this. Currently, the supervisor doesn't use it, but I think it's helpful to allow the supervisor to use that option.
I do have some concerns if we just put all the resource attributes into identifying, since some of them do seem like they belong more in non-identifying Just, like, based on, on, like, os.type and things like that, those don't necessarily need to be in identifying.
And also, like, the resource section users might add, like, any other ones that probably most of the time do end up in non-identifying. So if we… if we change that behavior, that would have some, I guess, impact on… on this.
**Jade Guiton** 22:27 Hmm. Yeah. I see.
**Tigran Najaryan** 22:29 I agree with that. I don't think we should be including everything into the identifying attributes. I don't… I don't see the need to do that.
And we have these controls in place for the non-identifying ones. I think they're good controls, right? So you want All the data that exists in the resource.
you specify this, and it goes into the norm identifying adjectives. I think that's the right thing to do.
**Jade Guiton** 22:56 Hmm, I see.
In that case… Hmm.
In that case, maybe the thing to do would be… If we really want to support the use case of… using separate, like, different identifying attributes would be to add a separate config option to say, for these resource attributes, I want them in the identifying instead of non-identifying. That's definitely more effort. Definitely more effort for a pretty niche use case, so…
**Tigran Najaryan** 23:27 It will give you more fine control over what goes where. I don't really know if it's necessary, to be honest.
**Jade Guiton** 23:35 Yeah.
**Andy Keller** 23:35 I think, I mean, we could default, like, the instance… ID… Into that list.
If we had a list of, Resource attributes that should be… become identifying attributes, and I would think that instance ID will be one of them, right?
**Jade Guiton** 23:58 Hmm.
So, in other words, you would make the… Include resource attributes option, the default… And then you would use that as the mechanism to insert Service instance ID and whatnot into identifying.
**Andy Keller** 24:15 No, I'm just saying, if you had… if you had a… a parameter, I'm thinking of it as just, like, an array of… of names.
That you want to be included in identifying?
From the resource attributes?
Alright, bye.
I guess I'm saying that service.instance.id seems like… A natural fit for a default value for that setting.
**Jade Guiton** 24:42 Yes, definitely.
**Andy Keller** 24:43 Otherwise, we end up potentially Copying that into non-identifying and having it in both places.
**Jade Guiton** 24:51 Yes, I think the current code already makes sure that When you add include resource attributes, it doesn't override any of the identifying attributes.
**Andy Keller** 25:02 Or, or duplicate them, okay, that makes sense.
**Tigran Najaryan** 25:05 Yeah, we should check then and avoid that.
**Andy Keller** 25:08 Maybe that's…
**Tigran Najaryan** 25:08 Yeah, it's definitely, yeah.
**Jade Guiton** 25:11 Okay.
**Andy Keller** 25:11 Yeah, so then that's not so much of an issue, and… probably the default value of it doesn't matter then, but I think that's… That's the shape of how that could work.
**Jade Guiton** 25:21 Hmm. Okay.
Okay, so, yeah, it sounds like… We don't really have a strong, compelling use case.
Right now… I guess my main concern, I guess, with this… Practical concern would be… When, at some point, the collector gains the ability to… Set up resource detectors.
It'll be for the host name.
I'd like to make sure that the hostname matches, but it's not identifying anyway, so… I guess it's okay.
**Tigran Najaryan** 26:03 Reserve detectors for its own telemetry, you mean?
**Jade Guiton** 26:07 Yes, that's in progress.
**Tigran Najaryan** 26:09 Yeah, yeah.
**Jade Guiton** 26:10 But yeah, right now we don't really have a good use case, so there's maybe not much of a point in adding this extra config.
**Tigran Najaryan** 26:16 Is it necessary, though? Does it need to be in the identifying attributes? It can… so let's say the resource detection is enabled, and the detected attributes go into collector's planetary, but they will be in addition.
to the built-in ones, to service name, instance ID, and things like that, right?
If… the OBAM protocol doesn't require that everything that is in the resource is included as identifying attributes. You only need to have attributes which are sufficient for unique identification.
And supposedly, the expectation is that these three attributes, service name, version, instance ID, the combination of those three is enough for globally unique identification of the agents. And that means that everything else in the detected resource can go into the non-identifying attributes, and that's okay, there's no problem with that. Using just the free service attributes.
We'll give you what you need in terms of this promise from the spec.
The red.
**Jade Guiton** 27:29 Right.
**Tigran Najaryan** 27:30 sure, it can be reported as additional information in the non-identifying attributes, and I think that's fine. I don't think… there's anything wrong with doing that. You can still have the host name, host, whatever, host ID, visible.
In the agent management server as well.
And it's fine, right? You have two buckets of attributes, identifying, non-identifying, but that's okay. The host name happens to be reporting… reported in the second bucket.
**Jade Guiton** 28:00 Yeah, that makes sense to me.
Yeah, okay.
Yeah, so it sounds like, yeah, there's not really… Much that we need to do unless someone really, really wants to disable these.
Beautiful.
**Tigran Najaryan** 28:17 I mean, doing this is wrong. If you read the spec, OpenTelemetry says these three attributes, the combination of these three, is expected to be globally unique.
That's a requirement. Now, if you do this thing, and it's obviously you break the promise.
break the expectations that the OpenTelemetry specification sets.
I say all bets are off, right? Don't expect that things are going to work correctly if you do this.
**Jade Guiton** 28:47 Right, and I guess we consider it, I guess, a saner default to… To fall back on something in that case.
Yeah, that makes sense. Yeah.
Although, I guess… Technically, if we're talking about this deck, we should also have, sorry, that namespace in there, but… I don't know how many people actually use that.
Alright.
Yeah, that's… that's it for my… for my point.
I think I'll probably…
**Tigran Najaryan** 29:14 Okay.
**Jade Guiton** 29:15 Pose the issue, and if someone really does come into that use case later, they can open a new one.
**Tigran Najaryan** 29:22 Noah, sounds good. Thank you.
Right, next, Stanley, you want to talk about the message attestation?
**Stanley Liu** 29:33 Yeah, thanks.
Yeah, so we got a lot of helpful comments since the last SIG meeting on this issue. So I think Dom just responded, like, a few hours ago in response to your last comment, but, just wanted to also reshare the proposal document, because I think a lot of the questions that you had about, like.
the architectural design of it, would be resolved in the, yeah, the spec proposal doc that he linked. So, and then if you have any other questions, can definitely help to clarify that.
But we just wanted to emphasize that, everything that we're doing in this proposal is also opt-in, so it wouldn't break any clients. And I think one of the questions that you had was, clarifying, like, what kind of attacks this proposal would prevent. So, we worked on putting together a private repository with, three reproducible attack scenarios that would show an op-amp-managed collector applying a config that the legitimate operator would have never authored, all under full TLS validation. So… was just wondering if you guys would want to see this. We definitely understand that attacks on the vendor side for a compromised server are less common, but we also found attacks on the client side that are possible that could compromise an entire fleet for a customer.
And these scenarios could be prevented with this proposal.
So… We felt that the risk for large vendors such as Datadog, Splunk, Dynatrace is, too high, we're risking this Compromisation, compromising for an entire fleet for a customer.
So we just wanted to highlight some of these issues.
I was wondering what's the best way to share this.
**Tigran Najaryan** 31:27 By the way, I completely agree with you. It's a huge risk. You don't need to convince me. I share the concerns. I would like to have some sort of a solution here.
It's just that I would like to understand your proposal about how this is solving better in more details, but I don't need convincing that this is an actual problem. I agree with you on that.
**Stanley Liu** 31:51 Okay, yeah, sounds good.
**Tigran Najaryan** 31:53 I just wanted to.
**Stanley Liu** 31:53 Just to put together more complete stuff, yeah.
**Tigran Najaryan** 31:57 Sure, if you want to share more, that's fine. I'll take a look at… I glanced at this response just an hour ago. I'll take a look at it closer, I'll think about it, and we'll respond to it.
I definitely would like to find some sort of a solution here to the problem. Again, like I said, I agree with your assessment that this is a big concern.
Would definitely help if we can have some sort of a mitigation to it in the protocol.
**Stanley Liu** 32:28 Yeah. Yeah, thanks so much. Yeah, definitely, it definitely helps a lot.
So, we're also working on implementation of the spec, so we, like, started working on forks and OpenTelemetry Go, CollectorContrib, and we also have an end-to-end test, so if it helps, we could open draft PRs if you would like, but if you want to wait longer before, like.
proceeding with that, that's also okay. Just wanted to…
**Tigran Najaryan** 32:55 I am not… I think at some point, example implementations or prototypes would definitely help.
at this stage, I definitely would like to, first of all, understand what exactly are the types of the attacks that we're preventing here? Yeah. So, and this helps, definitely.
And I also would like to understand what types of attacks we're not preventing, which remain to be possible, even if we implement this, and whether this is enough Or we need to go further than what we have here. So, that would be, I guess, the prerequisite for me. Is this the right design? If we agree on that.
Then, definitely, prototypes would be the step two, so that we then see what does that look like when implemented in the code.
it's a bit early, I don't want you to do too much work unnecessarily if we're going to change the design after the discussion, so it would be maybe a wasted effort if you do the prototyping of a design that we don't end up accepting, so let's agree, first of all, on what the solution and what the design, the architecture looks like, and then we'll take a look at some of the implementations.
**Stanley Liu** 34:14 Nice. Yeah, that makes sense to me. Thank you. We can, just discuss further on the PR, so if you have any questions, we can clarify that. Yeah. And then if the private repo is okay to share, just, like, we can add you guys as contributors if you or anyone else would like to take a look at the POCs that we added.
**Tigran Najaryan** 34:37 Yeah, okay, we can discuss that. Let's do the step one design piece, and we can talk about it.
**Stanley Liu** 34:44 Yeah. Does anyone else want to be added to the private repository? If not, I can add, Tigran, but just wondering if anyone else is interested.
**Tigran Najaryan** 34:55 Don't do it just yet. Oh, okay. I will let you know if I want to be at it. For now, let me think about the design, and I can comment on the PR. If I want to take a look at your private implementation, I will let you know. It's also… Definitely don't want to see anything you guys do, anything proprietary.
So I may want to see in some sort of an… can be a different repository, but something that is open sourced with some sort of open source license.
Yeah. Because if it's…
**Stanley Liu** 35:31 Oh, yeah.
**Tigran Najaryan** 35:32 Your proprietary thing that is confidential than comes with other… baggage that I don't necessarily want to get into.
**Stanley Liu** 35:41 Oh, okay, yeah, I got you. Yeah, I think, I was actually just referring to the attack scenarios that we implemented. They're not in the, like, proprietary repository, it's just, like, some, like, like, scenarios that we implemented in a personal repository.
So…
**Tigran Najaryan** 35:59 Okay, let me read this.
reply to you. If I need more details, I will ask for it.
**Stanley Liu** 36:05 Yes, sounds great. Yeah, thank you so much.
**Tigran Najaryan** 36:07 I definitely want others to also take a look at this. This may… I don't know, maybe, Andy, you have any thoughts, any opinion? You have a thumbs up? What do you mean by that? You want to?
**Andy Keller** 36:19 I will look at it, yes, I will.
**Tigran Najaryan** 36:21 All right.
**Andy Keller** 36:22 We'll look at it in more detail.
**Tigran Najaryan** 36:24 Thank you.
**Stanley Liu** 36:27 Cool, thanks so much.
**Tigran Najaryan** 36:33 Alright.
Andy.
Message size?
**Andy Keller** 36:38 We were asked a long time ago in a DM on Slack about implementing a max message size, And, I was gathering some more data around, what our max message size looks like.
I… because we use them for custom messages for some, you know, very specific uses, I've seen them as large as 25 megabytes?
10 seems to be more common.
of a max, but I'm… I'm a… I'm just a little concerned.
about… Putting a max in that's too low, and… and… You know, compromising functionality.
So, I'm just curious if there are other…
**Tigran Najaryan** 37:43 I think we ended up, yes, 64. We ended up with 64 as the limit for OTLP.
We could use… a similar number as the default for OPAM, which seems to be at least double of the number you just said? You said 20-something?
**Andy Keller** 38:00 I think, yeah, that should be safe for us. I just wanted to understand if there's anybody I'll send.
You know, is doing anything with larger payloads.
**JM Juande Manjon** 38:11 So, in my company, instead of doing a hardcode size of the message, what we are doing is adding annotations in the proto-definition, in the specs.
Saying how many items, how many repeat messages you can have. When you have bytes, what's the maximum, size of that particular byte.
So, in that case, you have more granular, say, so for this particular kind of method, the size, the maximum size this, and those are using metadata proto-annotation.
where the code can, read that metadata and generate the validation code automatically. So, if some reason you want to change the specs, automatically the… the CI.pipeline will modify and generate the code accordingly with the new specs. This is a clean design that helps a lot, and we don't have to worry about Coding that part.
**Tigran Najaryan** 39:05 I think, yeah, I think what you're talking about is also interesting, but it's different from what this one is suggesting to do. This is about the size before you try to decode. This is the entire payload.
Size, and if it's too large, Essentially, no attempt will be even done to try to decode it even, right? What you describe is applied when you're decoding, there is a repeat element, repeat field in the proto, and you limit how many repeat elements can be there. Again, I realize that that may be also useful.
But this is before all of that happens. This is… you receive a payload, you look at the entire thing, the size of it is above the configured limit, you refuse to even try to decode it, because it's just too big, essentially.
**JM Juande Manjon** 39:56 Right, but you said the pillow is also protob, right? So, you have a feel, it's tight bite.
So when saying you can't add an annotation for the maximum size of that byte's chunk.
So, if you receive more than that side, you won't necessary to decode, because it's all the scope.
And also, on the client side, if the message on the client side bigger than the maximum side, the open client won't send to the server.
**Tigran Najaryan** 40:29 Yeah, I get it, I understand what you're saying. Having limits for individual fields or messages in the… in the proto also helps.
we can have that discussion as well, but that's different from having the limit on the entire thing. You can probably have both, right? And in OTLP, for example, there's a limitation on the attribute sizes.
We could have something like that also for, let's say, for all pumps.
config file fields which tend to be big, you could have a limitation on what the individual config can be.
And in addition to that, you can also have a limitation for the entire payload, the entire encoded state of the… of that server-to-agent or agent-to-server message.
so that if it exceeds that, you don't even try to decode it. If you're a sender, if you're a receiver. Or if you're a sender, you don't try to send things that large. This is… this was added recently to OTLP, and this is where it's coming. The discussion was.
do we need to have similar capability to… to… to be in the no pump as well?
**JM Juande Manjon** 41:42 Yeah, I totally agree, we have to have bounding messages, so…
**Tigran Najaryan** 41:47 Yeah.
Okay, Andy, do you think… Having a limit like this, which is a multiple of what you have seen, multiple of the maximum you have seen.
I think that's fine. Yeah, 64. And it can be configurable, right? It's just a default. We still can't change it.
**Andy Keller** 42:08 Yeah.
**Tigran Najaryan** 42:11 I think that's fine. And we should probably apply it both ways, right? In both directions, from agent to server and server to agent, and I think it's reasonable to have the same limit there, because the exchange is mostly symmetrical size-wise.
**Andy Keller** 42:28 Sounds good.
**Tigran Najaryan** 42:30 Okay.
Anyone else? Any other, other thoughts?
Okay.
That's all we have in the agenda. Anyone else, any other things to discuss?
All right, thank you all.
Bye.
**Evan Bradley** 43:04 Hi, everyone.
