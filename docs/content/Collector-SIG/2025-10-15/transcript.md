SIG: Collector SIG
Date: 2025-10-15
Duration: 64 minutes
Zoom Recording URL: https://zoom.us/rec/share/65dXM6enu-O4oy2uXKTr96qFN9oD-wx45gkoS2mnhaOHP0eIvKErzLs1hoayUy8U.Jn3QNnfmMO8agRHA
============================================================

## Zoom Recording Transcript

Pablo Baeyens 00:04:28 8.
Dmitrii Anoshin 00:04:44 Hi, everyone.
Paolo, do you want to start?
Pablo Baeyens 00:04:54 Yeah, I can start, So, I filed a PR, that would change the behavior or of optional fields, so that we now have an enabled, option on each of them. The main… Argument for this is that right now, if you have an optional field that by default is enabled, there's no way to disable it.
So this tries to… to fix that by adding this.
Enabled, option.
I've applied it to every field that is optional, and not only the ones that are enabled by default.
just because I think consistency is… is better. But yeah, I think it's… it would be a big change. For example, it would change the way the… it would add a new way that the OTLP receiver configuration works, and so I want to… Want to hear from people, what do they think?
Dmitrii Anoshin 00:06:08 First of all, thank you, Pablo, that's amazing. I'm really excited about this change. And, yeah, I… I will review it, so… Thanks.
Paulo Janotti 00:06:19 I have a quick question, Pablo.
I, and I lost track of that many. We used to have enabled for components.
Because I think the proposal makes a lot of sense, but I want to be sure that we also have those for components, so you could put the higher level And have the same, the same experience, not only for the fields of the configuration.
Pablo Baeyens 00:06:53 So… I'm not sure what you mean, like.
Paulo Janotti 00:06:57 So, you could put, like, let's say, receiver OTLP, And right there, you could have enabled.
Pablo Baeyens 00:07:09 Right, this BR doesn't change that.
Dmitrii Anoshin 00:07:16 Oh, do you have a use case for that?
Paulo Janotti 00:07:19 I think it's the same, right? The use case will be the same, because if you want to control a specific thing, with some external that can evaluate you true or false.
Why not do that through the component itself?
Dmitrii Anoshin 00:07:33 But components are not instantialized if they are not part of the pipeline. So, essentially, you disable a component by removing it from the pipeline.
Paulo Janotti 00:07:43 Yeah, and I'm mostly asking because I don't remember the current status, but it seems to me that if you have a way to disable at the sub-level of the component.
Why… it's gonna be the problem of the pipeline if you disable and it's… it's split from the pipeline, but… at the same sense, it feels that very natural, like, why I can't just say, receiver zipping enabled, disabled, you know?
Dmitrii Anoshin 00:08:15 But in that case, we would need to… it will bring complication in terms of what's the behavior if component is disabled, but it's part of the pipeline, so we would need to…
Paulo Janotti 00:08:27 Yeah, that…
Dmitrii Anoshin 00:08:28 a lot of, like, things to keep in mind. Right now, it's been controlled by one thing, by pipeline. I don't… I don't think we start… I don't think we even instantiate components if they're not in the pipeline, so…
Paulo Janotti 00:08:44 Yeah, I think that's… I think that's the case, but… Just thinking convenience, Okay, you can override the pipeline on the command line.
But then you have to, like, you have 7 receivers. You want to disable the zipping on the pipeline, okay, you can disable on the command line, and keep the same configuration by removing it from the pipeline.
But you can't just set, the receiver… but to your point, and I think this is not related to the change, that Pablo is talking about.
But it's more on the experience of the user. I don't think it's very consistent having this difference. You know, I understand the implementation, but I think we can pursue that as a separate issue.
Pablo Baeyens 00:09:46 So, I think, as Dimitri said, the issue is probably more complicated, just because of the pipelines.
I feel like my PR is a step in the right direction, consistency-wise, because we already have some things that are controlled by enabled, while other things are controlled by putting this section empty, or not putting it. So I feel like it's a net positive in the end, and we should do it.
Yep.
Paulo Janotti 00:10:15 No, no, I agree. It's a positive change in the right direction, and I kind of went on an orthogonal here about this, but it's just from the user perspective experience.
Dmitrii Anoshin 00:10:28 We definitely can have an issue about that and discuss it.
Paulo, another comment on this one about us. So… we don't… still don't support scholars for optional, and so what's gonna be… what's the plan there? Just… just trying to confirm. We are not gonna have enabled field there, right?
Pablo Baeyens 00:10:55 So last time we discussed this, we were talking about using null to signify disabled for something like that.
I think we can do whatever we want, since we explicitly ruled that possibility out, when building a config optional.
we could do whatever we want. I don't think putting enabled is… is the right choice there.
Dmitrii Anoshin 00:11:19 Yeah, I agree. I'm just thinking that we need to probably Like, think about it.
for forward evolution of the optional interface. I'm not even sure that… optional interface is really needed for scholars. It's kind of… Unclear to me why you would not use a pointer instead.
Pablo Baeyens 00:11:46 So, I'll let… Evan speak about that, if he wants, but yeah, the use case we have right now is maybe, like.
the components ID for storage, stuff like that.
Dmitrii Anoshin 00:12:02 Okay, and yeah, if we have… Like, some roadmap for how we're gonna… what we're gonna do for… I don't know, scholars, it's fine.
Thank you.
Evan Bradley 00:12:17 So, for scalar values, I will talk about that after Jod, discusses her, bullet point item, but, I… I've been working on that. I… I think the… Main motivation is just consistency.
I'm not sure that… we have any use cases that strongly need it, but I think it was just kind of a matter of… You would expect that for any optional value, you just use this type.
Dmitrii Anoshin 00:12:47 Yeah, and now we are bringing a bit more inconsistency when we introduce Enable to the… To the structs, but not to the scholars.
So…
Evan Bradley 00:12:58 I see what you're saying.
Jade Guiton 00:13:01 I think for that part, it's kind of necessary for backwards compatibility, because, setting something to null is the same as setting it to nothing, just having an empty section. And at the moment, it's kind of expected that if you have a struct.
section, instruct field, and you, set it to an empty section, then it… that it would be enabled. That is the current behavior.
In a lot of places.
So… We could, in fact, choose to disable Structs with null as well.
But it would come at the cost of breaking backward compatibility and probably user expectations.
For… for some things.
Dmitrii Anoshin 00:13:59 Okay, makes sense. I'm still… it's still unclear to me if we really need optional for the scalar values in that case, if it's gonna be different than what we… gain by having… Not support, but… I guess it's not very strong, like, we can… we can… Keep it like this. And I understand you're… Argument, like, for backwards compatibility enabled.
constructs. It's not the case for scalars.
Jade Guiton 00:14:37 Right, I mean, yeah, I guess the question is… Like… We switched to using optional for structs, partly because we wanted to get rid of the pointers.
So I think it kind of makes sense to decide to do the same thing for scalars.
But… Yeah, I guess… So, does it work if you set it to null when you have a pointer to a scaler? Does that currently work?
Dmitrii Anoshin 00:15:11 Yeah, that's… I believe it should work.
Not 100% sure, but I don't… as far as I remember it, it should be fine.
So you have zero value for integer, you said 0, it's 0, you said, now let's, it's normal.
Jade Guiton 00:15:29 So in that regard, maybe… The inconsistency between structs and scalers is already present.
Because… if you have a pointer to a struct, and you set that to null in the… in the YAML config, I'm pretty sure it doesn't reset the pointer to null .
It merges nothing into the struct that's already there.
So if that is indeed the case, then I guess the inconsistency is already kind of present.
Dmitrii Anoshin 00:16:07 Yeah.
That's fine, I guess.
We can maybe summarize our decisions in summations.
I'm… I'm okay with having optional for scholars as well, with a bit different behavior. We just need to document that.
Jade Guiton 00:16:24 Yeah, definitely.
Pablo Baeyens 00:16:35 Okay, so I think we can… continue the discussion on the PR on MOB2Chat's topic?
Jade Guiton 00:16:43 Right. So, this is about a PR that, will introduce a breaking change in configGRPC and configHTTP.
Specifically the fields for setting the headers.
That are sent by, a client.
Or sent by our server in response.
The motivation here is that the hotel SDK declarative config.
has chosen to represent header maps in the config, not as a YAML map, but as a list of name-value pairs.
And so the related issue here is wanting to have consistency with that, to be consistent with that in the hotel collector component config.
By supporting this other way of specifying headers.
And, of course, there's a lot of existing configs that would be broken if we just switched directly to the new format, so the idea of this PR is to support both formats, so that there's no breaking changes for users.
But, while it is possible to do this without an API breaking change.
And I did a POC for that. It's… Pretty inelegant, and might make our messages worse.
So this PR, which is still a draft for now.
chooses another approach, which does lead to an API breaking change, on configGRPC and configure HTTP.
But the… advantage of this approach is that it isolates all of the logic into a new type with its own unmartial function, kind of like optional, instead of having to have a special unmartial logic in the parent struct every time you have… you have this kind of thing.
So… I guess I'm… I'm looking for… for feedback.
on whether people think the breaking change is worth it. API-only breaking change, to be clear.
In terms of… Keeping the code cleaner.
Compared to the other, POC.
Dimitri?
Dmitrii Anoshin 00:19:02 Yeah, the configuration for PCHTP is not 1.0 yet, right?
Jade Guiton 00:19:07 Yes.
Dmitrii Anoshin 00:19:07 Okay, in that case, I definitely support make and breaking change to make the code cleaner. I think it's fine.
And I would also rather suggest not keeping this state forever.
And if user specified the old way of setting headers through the map.
We would show them a deprecation warning, and at some point, we remove that capability before we make it 1.0.
Potentially.
I mean, I'm suggesting that I'm looking towards the cleanest, Implementation at the end, essentially.
Jade Guiton 00:19:52 Hmm. Yeah, that would be possible.
I would just need to add a, I guess, a… warning in the unmartial… That handles the map case.
Yeah, but maybe we can, I don't know, do that in a… I guess I can do it in this PR, the one.
Dmitrii Anoshin 00:20:13 Pretty young.
Jade Guiton 00:20:13 At least.
Dmitrii Anoshin 00:20:14 We can do it separately. I don't think vlogger is available in that Marshall function, but we can do some, let's say… But, like… We have…
Pablo Baeyens 00:20:25 And store the warning in a private field, and then log it once you have a logger.
Dmitrii Anoshin 00:20:30 Something like that, yeah.
Jade Guiton 00:20:35 Wait, so, when would you log it?
Dmitrii Anoshin 00:20:39 When did they go?
Pablo Baeyens 00:20:40 build the server or the client, I guess it's a possibility.
Jade Guiton 00:20:45 I see.
So, okay, special handling and configure HTTP and configure gRPC, yeah, that would work.
Yeah, although I guess it wouldn't be generic. I guess the idea here is that the PR introduces this new generic The, like, opaque map type?
Which is used for headers, but I guess could be used for other things.
I don't know if we can make the warning generic for that, but yeah, I guess for the headers, which is the part where we want to be consistent, I guess.
Yeah, we could do that.
Dmitrii Anoshin 00:21:21 Yeah, I would rather remove it going forward, because it also introduces problems how we… diserellies.
How we serialize the configuration if we need to.
I believe it's needed, actually, for a pump already, like… Current config, collector config.
serialization, so it might… A pump might run into some problems with this approach.
Jade Guiton 00:21:52 With the current approach of using maps?
Dmitrii Anoshin 00:21:55 No, not decent mass, but when you can… have one configuration which can be represented in YAML in different ways.
Jade Guiton 00:22:04 Hmm, I see.
Yeah.
And these… in this case, like, they should be equivalent, right? So is the issue that it doesn't round trip, or that… Opam doesn't report exactly what the original…
Dmitrii Anoshin 00:22:22 Great.
Probably, yes. And I think it's fine if user specifies the map, and we, like, a pump reports the new way of… setting the values, I think it should be fine. It's just, like, something that we need to look into.
Jade Guiton 00:22:38 Hmm.
Right, yeah.
Dmitrii Anoshin 00:22:41 And that's what I'm saying, like, it's better to remove it going forward than keep one-to-one mapping between internal representation and… And visual.
Jade Guiton 00:22:52 I see, yeah, that makes sense.
Mmm… Yeah, in that case… I guess the PR can be… can stay like this for now, and then I can create an issue for… doing this whole process of, I guess, deprecating the old way.
And then eventually removing it.
Dmitrii Anoshin 00:23:14 Sounds good, yeah, thank you.
Jade Guiton 00:23:22 So, yeah, that's about it. If there are… No other comments, and if… this approach sounds good, I'll mark the PR as ready for review. As soon as I figure out Why the contrib tests are passing.
Even though this is a breaking change, but yeah.
I'll do that.
And, yeah, I guess we can move on to the next point, which is Evan.
Evan Bradley 00:23:52 Alright, thank you. So, we discussed this at the, stability meeting a couple weeks ago.
And I wanted to bring it up because it occurred to me that if we cut scope a little bit, we can still pull off, doing, like, an unmartial V2. So, specifically what I found, and kind of what this commit is supposed to show is that we can basically use the scalar, marshaler and unmarshaller what do you call them? Like, options? Basically, we can have… Or we can use those interfaces to… basically do struct, on marshalling and marshalling as well. The one thing is that you lose, the ability to access the map.
So, if we're comfortable with that, this would be… basically, I could just rename the existing, interfaces to just be, like, you know, on Marshaller and Marshaller V2.
And it would work.
The… I guess the open question is whether we're comfortable… with the idea that this would… I mean, this is, so, ConfMax 31.0, so we have to keep the existing, on Marshall interface, and there's a lot of… components that use it. I did a search in Contrib and found… It says 125 files, so, obviously it's pretty widely used, but I've noticed a lot of the calls, Are just things like checking if a field is set or something like that, and we can basically do that with the optional type.
The… So, the unmarshaller would go through, it would see the optional field, and then when you're doing the, un-marshalling of the struct that contains that field, you could say, like, okay, does this field have a value or not?
And that wouldn't require access to the map, I believe. However.
If we want situations, and Pablo's, optional PR actually does this sort of thing, but if we want situations where.
structs support a YAML schema that isn't necessarily captured in the… The struct itself, aka, like, map structure can't… Just based on the struct alone, decode the map.
then this wouldn't be a good long-term, solution. The… the thing that makes me think that it might be okay is that, I wouldn't mind… trying to more, strictly enforce that, config structs are declaratively, configured. So basically, the config struct has to, explicitly state what options it supports, and we don't provide access to the map. I think that would… it would clean up the unmarshalling functions.
And would also make it easier to… pull in config structs and, programmatically reason about them. So, for example, if I wanted to generate a schema based on the config structs, I would be able to do that through reflection if I used… If the struct declares all of the fields it supports. If it doesn't include those, or the schema is somehow different, then you lose that ability.
Okay, that was a lot of talking. I'm looking for ideas here. Jad, I see you have your hand raised.
Jade Guiton 00:27:21 Yeah, so I… I guess my initial question is, what do you mean by losing access to the map?
Like, if scalar and marshaler… if the scalar and marshaller method gets back the original value from the YAML, why can it not access the map.
Evan Bradley 00:27:41 So, okay, so you're, you're decoding… let's say you're un-marshalling either a scalar value or a map value, you… what I do right now is I call decode on the value before giving it to the un-marshall method.
So what you get is just the, like, the go value, so that's just, like, an any type value.
You would either get, in that case, like, a scalar, like an int or a string, or you'd get a struct.
There's not, like, a map equivalent, necessarily, for scalar values, so you would need to, like… that would… It would need to be added in extra, and that's where I was thinking that the… the two interfaces would be better, because for struct values, you just pass the map, and for scalar values, you just don't give the map.
So when I say you don't have access to the map, the scalar on Marshaller interface right now is just data any, and that's, like, the already pre-decoded by map structure, data, and then you can, you know, go into that and do any tweaks that you want to.
Before, the struct is, you know, made available, or the config, is made available, but… If we went with that, again, you wouldn't be given that conf, because we would be treating scalars and structs the same way.
Jade Guiton 00:29:00 Hmm. So, the decode function… Well, what mmm… I'm still a bit confused about why… The skiller on martial art wouldn't be able to just get the go value, the any, for… Or a map.
But, to get to the second point I wanted to make, which is that I think kind of the whole point of the UnMarshall interface initially was to support Cases where the YAML doesn't match the struct?
So I feel like not having that option would be kind of problematic.
Because, like, that is… it seems to me, like, while we've used it for things like defaults and stuff, and we're kind of moving away from that, it seems like it should still be usable for more extreme cases where there is… where there isn't a clear… match…
Evan Bradley 00:30:00 I think that's valid, and I think… yeah, no, I think that's a valid point to take, and if that's the direction we decide to go in, then that's… I mean, it's easy, we just… we make the scalar on Marshall Interface, and we're good. I think the reason… so the motivating reason why I think it would be okay to… not provide that is, again, the, like, requiring structs just declaratively say, like, this is the configuration schema I support.
And… you can, you know, do some tweaks to that while unmarshalling, but for the most part, the schema itself remains the same. So, maybe you can analyze values and say, like, okay, I'm gonna swipe… I'm gonna slightly switch this up, but you have to declare your… Like, here is… like, I could take… I guess my goal is I could take a… like, collector config struct tree, and then generate a YAML schema from that. And you wouldn't be able to do that if… You have, like, procedural code in the unMarshall function that… Might modify the schema.
Jade Guiton 00:31:07 I mean, there's already kind Not the case with optional, right?
Evan Bradley 00:31:12 To… so, yes and no. Optional doesn't, like… It… it modifies the go structure, but the YAML structure doesn't change because of optional. Like, if you add or remove that, that doesn't change anything for the valid schema. I mean, if anything, you could say that this value is optional, you could annotate it, but the optional type itself doesn't… Change what you're… like, what keys you're allowed to set, if that makes sense.
Jade Guiton 00:31:44 Right, but that's a problem if you want to generate a schema from a struct using reflection, because you're going to have this extra struct in the middle that has the field, but it doesn't add anything in the YAML. It's somehow transparent.
Except when it's not, which… with the enable field, for example, that Pablo is in the process of adding.
Evan Bradley 00:32:06 Right. So, the change here would be that the enabled field would need to be a field on the optional type.
Which again, I think is another reason why we need to, kind of weigh our options here. But… You could determine through reflection that the optional type is transparent, because it wouldn't include any tags.
Like, it doesn't have any map structure tags for fields on it, but you could still recurse… I think you would be able to… I guess maybe that would be slightly difficult.
No, no, you definitely can recurse, because if it implements the Scalar and marshaller, you can get the… or Scalar Marshaller, you can get the type out, and you know that that type is a child of the optional type. So you both know that you have optional, you can look at its fields, it doesn't have anything, and you can get its type out and know that that's, like, the nested thing. That might… Be slightly business case specific, because you would need to know how optional works, but, regardless, I think it… you could still get a… you could programmatically derive a schema from From that type.
Jade Guiton 00:33:13 Hmm.
I see.
I'm not entirely convinced that it's… Worth… it?
I mean, maybe it is worth it, but, like, it would be a pretty big departure from the whole concept of offering an unmarshalled method in the first place.
I don't know what, Pablo, you think.
Pablo Baeyens 00:33:36 Boom.
I think we probably want to look at the… and Marshall functions that are in Contrib and see what they do. I can think of another use case that maybe we could score differently, but we don't support right now, which is… fields that are deprecated and renamed, maybe? So on the data exporter, for example, we have some fields where we change the name, and so we keep… a custom Marshall function so that, we can log a warning if the user tries to use the old name, and just, like, or, like, error out with a specific error that says, like, hey, this was renamed to that.
And I wouldn't be surprised if there's other cases that I'm not aware of that are also… right now supported through the MRSL function. So I would like to… to see that.
And then, another thought that I had while I heard.
YouTube. Talking about this is, There were some people that were not in favor of having an enabled field within the Go struct of the config optional.
optional struct.
Because it was seen as sort of, like, a leaky obstruction at that point.
I don't have a strong opinion there, but… Yeah.
Just as a data point, I wanted to plug out.
You could always… You could always have a private field that has… public subfield called Enabled. I don't know if… Evan's proposal would allow that, but that's one way in which you could still have a public field.
Evan Bradley 00:35:20 Would map structure be…
Pablo Baeyens 00:35:22 Maybe that was confusing.
Evan Bradley 00:35:24 Well, no, if it's a private field, I don't think map structure can see it, because you can't see private fields through reflection, if I remember correctly.
Pablo Baeyens 00:35:31 Right, yeah, so it would be, like, And Marshall would have to… connect the dots in some way. Like, it would have to say.
Evan Bradley 00:35:39 Oh, I see what you're saying.
Pablo Baeyens 00:35:41 Map it to this private field that has a public enabled field.
Evan Bradley 00:35:45 Okay, I'd have to think about that. I mean, the goal would be that you can, through reflection.
derive the schema of the config. As for doing things like deprecations and migrations.
I have another idea for how that would work. If you remember when we were talking about config templates… My thought is that you would essentially offer something that goes… that works like a database schema migration.
that does this with, GoTypes. So basically, you would have, like, you know, prior, you know, V1 of, like, the Datadog exporter struct, and then V2, and then you would provide something that would translate between those two structs, and you would provide that to the collector, and it would be able to… I'd have to think about it more, but it would be able to basically… un-marshall the config, and then run these transformers on it to get the… the migrated config. Obviously that's a little bit more work than just working on a map, I don't know, I mean, that's a separate discussion.
Pablo Baeyens 00:36:53 to me, like, yeah, the problem I see here more is, like.
we're going to find more cases like that, and we're going to have to do a lot of work to support all of them, and that may be fine, like, maybe the current and Marshall function is not great, but, I, for example, wouldn't want to delay the 1.0 work on having all of those available.
Evan Bradley 00:37:17 So, oh, yes, so, agreed, but that, I… so, how about this? I don't feel particularly strong about this, because even if we do make the… the functions, or the interfaces that we introduce to support scalars just support scalars. We would need to deprecate the existing unmarshall function So, if we do… if we go with Unmercial V2, where it supports both structs and… scalars, it will need to work in tandem with V1, so V1 will continue to be supported, and then we would migrate whenever we do a collector V2 or whatever. So that won't delay Collector V1, But, I guess the reason I'm saying that is I think that we can remove that from consideration. I think the question is more so, if we like the flexibility of… Giving component authors that conf.
then I think we should just stick with this for scalars only. We stick with our existing interface for structs, and we just move on for now.
Pablo Baeyens 00:38:18 Okay, yeah, so in the interest of time, I think the next step, at least in my mind, would be to look at the contrib usages of Unmercial, and see what use cases are there, and that can help us decide, the thing that you just said.
Evan Bradley 00:38:33 Yep, Okay, yeah, no, I just… so that is my next step, I'm going through and doing that right now. I'll put an update in my PR, I just wanted to get some initial thoughts, just to make sure that I was headed in the right direction, but thank you.
In that case, Bogdan, you're next.
Bogdan Stancu 00:38:52 All right. Well, I've been told that I should talk about this here in the meeting. I'm looking for sponsors for the Circuit Breaker extension.
Which, well, I, I put the… the link in the meeting notes, and just for a small presentation, I guess, is this would be used mainly because we… we have… well.
Our use case would be, that we have separate Hops, several… more… more than one set of… sets of collectors, and… Going from the clients to the backends.
We have, well, experienced that As the signals go through this pipeline of collectors, if they… end up at the end, and the backend is down for some reason, then we… I mean, it's… it's easier to lose data, because the queues would, buildup. That's one thing, and the other thing is that, All the collectors, apart from the last one would just answer with 200s, so the clients would not see anything wrong in their collectors.
And this is proposing a circuit breaker extension, which… would… kind of… Probe an endpoint.
Either the backend itself or collectors between them, and if the backend is down, then that state would propagate all the way to the clients.
Which… Because it's a smaller load on… in their namespace, it would be easier for… Us.
As a whole thing, to not lose data.
I hope I described it correctly. And I'm… well, I'm asking for sponsors.
For that. I also have… I mean, we have this deployed for authentication, kind of, the same… the same use case, but just for authentication, and it works well. And I would like to have that implemented into this somehow. I haven't thought of it very well.
But initially, I'm just, I'm… I'm just asking for opinions on just service health.
circuit breaking.
Jade Guiton 00:41:23 Out of curiosity, for the use case of… propagating… Back-end errors, like the backend being unavailable back to clients.
have you tried using the wait for results?
option in the queues, in the… assuming you're using the exporter helpers… Queuing mechanism?
Have you tried the wait for result option, which… If I understand it correctly.
Would wait until the exporter has… actually tried exporting, before returning 200, to the client.
Bogdan Stancu 00:42:03 Hmm… no.
No, I didn't know about this option, and I mean, I was under the impression, because receivers and… because of batching, receivers and exporters work kind of asynchronously, so you cannot report from the…
Jade Guiton 00:42:21 put it back.
Bogdan Stancu 00:42:22 Back to the receiver, because… Yeah, but it's not the same batch.
Jade Guiton 00:42:27 Yeah, so I don't know how this interacts with batching, to be honest. But yeah, the wait for result option is a new one, I believe.
Which, kind of… Bypasses this async nature.
We still have a queue, but the idea is that the…
Bogdan Stancu 00:42:45 Okay.
Jade Guiton 00:42:45 The call for inserting into the exporter doesn't return until the exporter has actually finished.
Bogdan Stancu 00:42:52 I'll look into this, this is interesting.
J jmacdonald 00:42:56 Yeah, I can describe that briefly. There is now support in the exporter helper queuing batching mechanism to properly apply back pressure, if you will, which means having the option to return an error from export through the batch to anybody who put data into the batch.
And that means you can block until the export succeeds. When I read your issue, I wasn't sure whether you were aware of it, but, you know, you could still make the argument, maybe, that, like, it's… there's a lot of work downstream of just, like, letting data sit in memory or go to a disk.
And if I… if you really want to short-circuit, you… you could probably make an argument for your component anyway, but I think you should take a look at that feature.
The other… the other associated one that I'm aware of, which is, I would say, new in the last year, is to block when the queue is full.
So you set two new Booleans, block on full and wait for request. It means you have back pressure, and that means you won't lose data just because the sort of down… the back end is down.
You'll still lose data, or eventually you'll drop it, or you'll eventually cause downstream… or your upstream consumers to time out, or something like that. But it does give you more control.
Bogdan Stancu 00:44:14 Well, this is great.
I will look into that. But as you said, I mean, the proposal still stands, I think, if anybody wants to use it.
I'd be interested in implementing it, just looking for sponsors.
Dmitrii Anoshin 00:44:28 So, we had a different, like, as Josh mentioned, we… for your use case, you potentially can use block on Block an overflow, or, like, blocking at all of the requests, essentially, with those two options, but, We… like, I remember we had a use case for a similar capability, but not, like, for every request.
But specifically for tokens. Essentially, when you send it some kind of, Authentication token with the context.
Instead of just passing through all the data through the pipeline, there would be some extension that would try that token first, if it's new, against the backend, and would remember it.
And just don't pass any other data, going forward. So, like, it's pretty much similar to your use case, but instead of, like, having, like, either pass or block for all of the requests, it would be kind of a hash map, per, let's say, token.
Bogdan Stancu 00:45:37 If you, like, if you pass this token, it'll… it'll…
Dmitrii Anoshin 00:45:42 block all the requests, and it'll respond pretty much with the same responses from the backend. It will be, like, not permanently, it will, like, leave for some time, then it would disappear if no requests are coming.
Bogdan Stancu 00:45:56 Yeah, yeah.
Dmitrii Anoshin 00:45:57 Something like that. Does that make sense, that use case?
Bogdan Stancu 00:46:00 It does, and I… I mean, I… I don't know what use case specifically you're… you're talking about, but initially, when I first started doing this, like, half a year ago, OpenTelemetry, I mean.
without knowing how it works, I did open a PR with exactly what you're describing, so we… you might be talking about, what I did. I… I don't know. But it… we have that. It was an early implementation, but we have that, what you're describing.
Dmitrii Anoshin 00:46:26 So, essentially…
Bogdan Stancu 00:46:27 Specifically that.
Dmitrii Anoshin 00:46:28 Yeah, the idea is that some tokens can be, like, can expire, and it doesn't make sense to queue them forever, and retry them, etc. Once token expired, we want to just, like, remember that, and… You use that extension on the receiver side, so receivers just, like, respond with the same response every time.
Is that the same equipment?
Bogdan Stancu 00:46:52 Yeah, it might be a PR that I did open with before. I mean, I just opened it and then closed it, I think, without… doing anything, like, no changelog, no nothing. I didn't know how stuff works, but yeah.
Dmitrii Anoshin 00:47:05 But I believe that can be generalized for your use case as well, so we can have pretty much same extension for both use cases.
that's… if we can have something like that, yeah, I would… I would be willing to sponsor it.
Bogdan Stancu 00:47:26 Alright, well, we'll have to, see how it, If it does anything more than what the other options discussed.
Dmitrii Anoshin 00:47:36 Yeah, but if you had already implemented that PR, and if you have that need as well.
So, it would be great if you can… Oh, yeah. If you still need it, and you want to incorporate that in that receiver, in that case, I would be happy to sponsor it.
Bogdan Stancu 00:47:52 Alright.
Dmitrii Anoshin 00:47:53 Thank you.
Thank you.
Bogdan Stancu 00:47:56 And I had another point, which is kind of similar to this, to this, not similar, but tied to this, is that we.
Dmitrii Anoshin 00:48:04 I'm sorry, we have some raised hand. Yeah, yeah, I don't want to say something.
Bogdan Stancu 00:48:07 Oh, study. Yeah. Sudi.
Yaten Dhingra 00:48:11 I would just think that if any working development process of this component is required, I would be… I would also be happy to help in that.
So, yeah.
Bogdan Stancu 00:48:24 Thank you.
All right, I'll, go to the next one, which is, as I said, tied to this, is that because we have this, middle, kind of.
parts.
collectors that work independently do some processing. It has been pretty hard for us to define SLIs just for that specific portion, because, let's say some user, starts sending wrong authentication, The metrics that are defined don't easily allow us to track the health of that specific part, because let's say the backend is rejecting them, the… what was it? Let's say metrics. The exporters, then… I had it here, but the metrics that should define if the collector did send something, are not… talking about sending, it's also sending and being accepted, so it was, yeah, we don't really care if the backend accepts what we send.
We just want some metrics that would define the health of this portion of the pipeline, and… As long as everything that we receive, we send, it's fine.
And, yeah, well, this isn't just… I mean, I… I don't expect, a change, I guess the metrics are good enough, but I was ask… I wanted to ask if anybody had problems like this, and how they, fixed them, because, yeah, well… also, I think the failed ones might also include retries.
So… We would end up with more… Signals being sent, then received.
Dmitrii Anoshin 00:50:35 This might be confusing, we need to clarify that in the documentation, but we don't report, tries of the retry… of the retry component, so it's… if it's… if it's metric report says something has failed, it fails like, I'm including all of the retries, so…
Bogdan Stancu 00:50:57 Hmm.
Dmitrii Anoshin 00:50:57 Once we tried 5 times, it only, reward 1 point.
Bogdan Stancu 00:51:03 So it would be safe for us to just add stent plus failed?
And compare that to how many we received. Yeah. And if they are equal, then all is good.
Dmitrii Anoshin 00:51:12 Right, exactly.
Bogdan Stancu 00:51:14 Okay, alright.
Dmitrii Anoshin 00:51:16 Yes, you have some, like, companies that would filter the data.
Bogdan Stancu 00:51:23 Perfect.
That was it from me. Thanks a lot.
Douglas Camata 00:51:30 So I… I will give a brief overview of my point. In fact, I just want to call some attention to a PR that I opened to the releases repo.
adding Linux packages, to the OPMP supervisor, so deadband, RPM, the general idea is that we have a system D unit, like a service, right, for starting the supervisor. It doesn't go together with supervisor configuration.
Collector configuration, or a collector binary.
These, these all have to be provided by the, user.
And the unit is configured in a way that it won't even try to start unless there is a supervisor configuration there.
And, yeah, this can be provided by users using drop-ins, so they can kind of merge their own customization into the unit, so they can provide their configuration in whatever way they want. They can use system decreds to make it very safe in terms of security, right? If they want. They can also just hardcode everything directly in the config file, use NVARS, Just like if it was a standalone or Kubernetes deployment.
And, yeah, my motivation is just that At my employer, we want to do this anyway.
So why not send upstream and give everyone The same thing for free.
So if anyone is interested in, reviewing, besides the assigned reviewer and… bother people from the releases repo that are often reviewing things. Or if you have opinions, suggestions on how to… how to make it better, if you know a bit more than me when it comes to system disservices, highly appreciated.
Antoine Toulme 00:53:53 Yeah, that's… that's interesting to me, I'll review.
I think, in general, we… we do need, this is a theme for at least a year, is to make the collector and all of OpenTechry easy to adopt, and that participates, so… Worth it.
Douglas Camata 00:54:11 Awesome, thanks.
Paulo Janotti 00:54:14 Okay, I think in the next, just, it's more like a heads up, I think we are running for a long time Windows 2022, Together with Windows 2025, and now I added the Windows arm to the test matrix and contrib.
Right. And, I think, there is not much value at this time. We… the kind of API that we use is kind of very standard. We installed two APIs that we could be running on very old Windows.
So I'm planning to kind of start to open later this week PRs to remove Windows training.
22 from the big test matrix. I'm gonna keep some kind of smoke test on that platform. If anyone has any concern, please, let's discuss this on the issue, or it's like, it's more just a heads up that I'm planning to do that.
Thank you, Josh. You are.
J jmacdonald 00:55:35 Hi, I wasn't paying attention to the order. So I put this, link in the end, since I thought there might be time, and there is. This is an RFC that I've written. I wrote it months ago, when I was originally working, on prototypes for what became an effort to add rate-limiting extensions and or memory-limiting extensions. There is already a memory limiter extension, but it is hardly quite fleshed out, and I had been doing this work earlier in the year. I intend to get back to it. The RFC was written to kind of capture everything I had learned through a few rounds of feedback with several reviewers who were more familiar with the codebase than me. And if it comes to adding an extension in the collector codebase, there's quite a lot of, sort of, like, knowledge that you need to pick up. So I tried to write it down.
To help anybody who's writing an extension, or adding a new extension, or testing an extension, for example.
I do intend to come back to my rate-limiting work, but my original motivation to get in there in the first place was to get memory limits working. It is pretty important when you have, for example, this wait-for-result mode set, that you have a total limit on pipeline volume, so that you can't accept new data back at the receiver.
And the… there's… if you follow the links.
This RFC was validated by the large prototype that I had built on, limiters.
extensions for limiting. So, I used the rate limit example in the RFC, and actually that's basically the API extension that I would propose for rate limiting. And I have in my drafts earlier as well, memory limiting APIs, sort of draft extension APIs. So… Why do I write the RFC? I think it's helpful. I want that merged. I will continue working on limiters, especially if we can get that merged.
So thank you for listening.
Dmitrii Anoshin 00:57:41 Thank you, Josh. I started reviewing it, and at some point got distracted, and it's like, I have some comments, but I haven't.
We'll flash them. And, yeah, I do agree, we definitely need to provide all of these guidelines and, like, all the… not… Like, notations that we established.
I'm… I'm just curious, is the RFC… like, probably it's a question to Pablo. Pablo, you've been involved in RFC's process for a while.
Is the RFC right place to put those guidelines, or it has to be a separate doc? Because RFC is something that we intend to introduce, right? Not something that we, like, we provide some guidance.
Pablo Baeyens 00:58:27 Right, so an RFC… I mean, the reason why we added the RFC process was to Try to resolve these agreements in some sort of structured way, where we needed multiple approvals, and there was a specific process where you need to wait a number of days before merging things.
I… Don't have a strong opinion as to the… Like, whether this… this falls into it or not.
whatever helps move it forward, like, pragmatically is what I… what I think we should do.
J jmacdonald 00:59:09 Maybe I would recommend that we… I think of it as an RFC in the sense that, you know, I did find examples in the code that led me to think this is the way we do things, but I also found quite a number of inconsistencies. I also found a few sort of simplifying, statements I could make, like, just general improvements across the board, across the codebase, where I think we could tighten this up.
So, in that sense, I'm… I am actually staking out a position. I'm changing… I'm saying we can change the code to follow what's written here, and if you go looking closely at the details.
what we have is not consistent. It's close. It's good, it's just not quite there. So one example that's easy to follow is, I found myself wanting to just, like.
We construct these extension interfaces by functional style, so you pass in these functions.
But there's a common pattern where the function I want to pass is a singleton that's just going to return a constant value, especially for config structs, and type values, and various other constants that we embed in these extensions, where there's really just a field, but because it's an interface, you have to make a method. So now I've got a method to represent a field.
And in my code, I just want to pass a field, which is a constant value. So, my proposal says that we're going to add a self method on any type of value that commonly gets used in an extension. So, types have a self method. Component ID has a self method.
Anything where you're going to ask the extension for a type, or a component ID or a config, those get self-methods so that it's easy to reconstruct new implementations of those interfaces. That's the type of thing that I am sort of changing.
And since we have one more minute, Bogdan Jrutu gave me feedback on my earlier draft of this, saying you've got to have the functional option pattern.
I don't agree that we should always have the optional pattern. The Go SDK in OpenTeometry has a different document. If you want to nerd out on this, you can go read theirs. It's in the contributing document. It says how to add an option, how to add a config struct in the Go SDK. This is a different approach, quite different, but similar.
And I wrote it as the RFC. What I would do, or recommend, is that we put a link to it in the contributing document.
with a paragraph, like, saying, this is detailed, we wrote an RFC on it, and then you can link to the RFC.
That might work.
That's… that's what I have.
Dmitrii Anoshin 01:01:46 Sounds good to me. Thank you, Josh.
J jmacdonald 01:01:48 Thanks.
Pablo Baeyens 01:01:49 Thank you.
J jmacdonald 01:01:52 Well, I think that's it. We've hit the hour. Good job, everyone.
Pablo Baeyens 01:01:58 See ya.
