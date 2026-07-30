SIG: Profiling WG
Date: 2025-07-24
Duration: 62 minutes
============================================================

## Zoom Recording Transcript

Florian Lehner 00:00:26 Hey?
And I guess, welcome to the North. Congratulations to the new job.
Jonathan Halliday (IBM) 00:00:37 Hello!
Felix Geisendörfer 00:02:22 Hello!
Florian Lehner 00:02:26 Bye.
Frederic Branczyk 00:02:56 Hey! Hey!
Felix Geisendörfer 00:04:31 Yes, we're a couple of minutes in. But me speaking up today does not mean I'm volunteering because I have a really bad cold. So unless you all want to hear me cleaning my nose throughout the entire meeting, I I would suggest somebody else step up today and lead the meeting.
Florian Lehner 00:04:53 I can try to volunteer.
Thank you. No one wants to jump in. Okay, then, I think I would just start. We are roughly 5 min past scheduled time.
1st approach is reviewing action items. 1st action item is review Prs, 6, 7, 2, which is about dictionary table encoding consistency improvement.
It looks like there was no updates since last week.
If I see the Pr correctly does, did does someone, or did someone actively work on this, or did review it. Please pick up.
Alexey A 00:05:53 This, Alexi. I have it on my list, but I haven't looked at it. I think there was a discussion about units in particular, if I remember correctly.
Jonathan Halliday (IBM) 00:06:02 Yes, I'm kind of regretting the way I titled this one because it started out life as a very, very simple change. The comments to deal with. How we index.
and to say that all the all the fields have a 0 element in them.
And that was approved. It was fine, but then there was some scope creep, and it got into a discussion of what we do with key values and units.
and this issue that it is possible, because of the the dictionary.
that we have the same key, but different units because of the semantics of the the units field. Currently, you can't represent that.
So we need to either decide that we just can't represent it. And we leave things as we are, or we need to change the encoding so that we can represent it.
Alexey A 00:07:00 Yeah, I think it's, I think it's a good discussion. And we we need to decide something.
because, yeah, I thought that a single metric.
We'll only have one unit. But and there also, I think there are 2 different cases. One.
One case in particular is like, what if it's just like microseconds versus milliseconds. So this metric, the the unit, is actually even compatible, like you could still merge it. But also we could have just things that are named the same, and they are, I think, like I, I don't have a good feeling how heterogeneous profiles can be in general like is this.
how likely it is. But I think in general it's it's not impossible, right that that there will be units.
Jonathan Halliday (IBM) 00:07:53 Yes, that's my concern, I I think, for the well defined hotel stuff where there's strong semantic conventions, and they do sensible things like putting, you know, underscore bytes at the end of a name to indicate what the unit is, even without separate metadata for the unit.
They're gonna work fine.
My concern is that this is sort of free form stuff where users can put in whatever they like, and they're not always going to be that disciplined.
So I think we need to retain the flexibility at this low encoding level to be able to encode anything they throw at us.
Alexey A 00:08:24 Does open telemetry require kind of like fully qualifying attribute names I don't know with company domain, or something like that. Is there any sort of like. I don't think so. I don't. I didn't see that in semantic convention. Well, except like sometimes like people prefix with things like with azure or aws.
Josh Suereth 00:08:44 Yeah. So the the rule for that, Alexi, is we. We require what we call a reasonably unique namespace in semantic conventions. Only.
So again, there's a difference between opentelemetry itself and users of open telemetry.
So for open telemetry provided instrumentation, we rely on a reasonably unique namespace which is in in extremes. Might be like company name dot product, right? But generally, for, like, you know, things like Linux windows, we just have them raw. Java. That sort of thing.
The the attributes, though, could be anything when users provide it. We provide no restrictions there. It's not like, you know, Java packages where you kind of force the ecosystem to be a certain way, we let it be open.
Alexey A 00:09:29 Okay, yeah, then, I think we need to figure out a way how to specify unit per attribute, basically.
Florian Lehner 00:09:39 Sorry to interrupt and go before you, Felix. Looking at the auto semantic conventions. Most of the conventions that report something. Do have a units field in the semantic convention, so units field can be either account byte second or millisecond. So for the specified attributes, I think we have something, but if attributes are not well defined, I think that's that's the church. But then, again.
if someone decides to use Msec instead of instead of Ms. For milliseconds. Then you can expand this topic quite a lot.
Felix.
Felix Geisendörfer 00:10:31 Yeah, what I was gonna raise. But it's probably come came up in the comments already. But I I think the main reason we're doing units is because people have had some right. That's why we put them into our format. Is that correct?
Alexey A 00:10:44 Yes.
Felix Geisendörfer 00:10:45 And I guess the main reason beyond that is because we might imagine people to create new profile types and wanting to express the the units used in those. But wouldn't we want those people to essentially contribute to semantic conventions if they want their things to to work well, and as you've mentioned Florian there, there's already an table column to specify the unit, I mean. That seems like the simplest pass forward. I would guess I'll let Josh.
Josh Suereth 00:11:15 Yeah. So the units you're looking at are an explicit field in Otlp.
Not only is an explicit field, it's part of our metrics. Protocol Api. So like when you see those units of bytes, sequence counts that sort of thing. For the most part, it's not necessarily an attribute. It's actually on a metric.
and we have an explicit unit column there, and we ask users to use the standard units of measurement from I forget what the website is nowadays. It just changed domain names, anyway.
That was a decision made for metrics around Unit. So when you're looking at those semantic conventions, you might be looking at metrics as opposed to looking at raw attributes.
Today, opentelemetry does not have a notion that a raw attribute has a unit as a separate thing, that it would like present and and contribute.
we also have a lot of complications around unit with metrics of things we didn't deal with that. Customers and users want, like.
you know? I can have the same metric name with 2 different units being reported. And it's awkward.
right?
What do you do there. At least you have it on the wire, but we still haven't sorted it so I wouldn't say opentele entry has a clear story on unit here.
but I will say that where we have unit it is explicit. It's its own field. It's in the protocol. I don't know if that link's the best one to show you. But I can also show you in the protocol where where unit shows up. If that helps.
Felix Geisendörfer 00:12:44 Do. Do you have a opinion here? What we should do? Just given that you have some.
Josh Suereth 00:12:51 Yeah, I, personally, I think you one of 2 things should be true.
One is when you define a semantic convention, you pick a unit for it.
and that is documented only in semantic conventions. And it's not put on the wire. And everyone who uses that attribute should be specifically using the same unit.
for if you need it to be open where people can provide different units, or like, you know, they might have different meanings. And you want that to be put on the wire in the protocol. Then you should make an explicit field for unit.
and probably following the Metrics Convention for that.
I don't. I don't know if that also makes sense for you, but if you want to see, like the standards, units of measure.org, that's what it comes from.
That is the standard that we went for for our unit. And there it is in the proto, as a as a link for you.
Jonathan Halliday (IBM) 00:13:48 So for what it's worth. I think my preference is to use a message which I think I termed key value and unit.
So in the link I posted in chat.
there's a data structure that is what I would term perhaps dictionary native in that it also takes the the string for the key out of the data structure and puts it into the string table. So it's space efficient. If the the key gets repeated and it just has an optional field. And the comment just says.
If if the name alone is not enough, I if it's not no, tell one where you can look at the name and know what the unit is from that.
Then set this field with the the unit value so on the wire. If you don't need it, it it's invisible.
but it's there as an optional thing.
If we need to encode the unit.
Alexey A 00:14:46 It's kind of close, I think, to how people often codes it right in the in the label message.
Florian Lehner 00:15:14 I also do have a slight preference to the proposal Jonathan, have with the key value and unit.
so it always ties them together, and would also make parsing easier. I would say, if you extract something and directly can tell, hey, that's in unit, whatever. And visualize.
Yeah, I like this approach.
Jonathan Halliday (IBM) 00:15:49 Okay. So this one's been open for a while and hasn't moved. I think the best thing, then, is probably for me to update the Pr, so that instead of just being a comment, that's, you know, actually in the Pr.
And then poke people to please review it again.
But unless there's dissent. I think we can probably consider this one done.
Felix Geisendörfer 00:16:09 Sounds good.
Jonathan Halliday (IBM) 00:16:11 All right action on me to update the Pr.
Alexey A 00:16:15 Just a quick thought on this. In this, in this message, Jonathan, would we even want in theory, put any value into its own dictionary as well. Because I I it's just most like thinking out loud. But I just wondered.
Jonathan Halliday (IBM) 00:16:31 Any value is effectively a couple of the the data type and the the value, because Protobuff needs to be able to to know what type it's decoding.
Alexey A 00:16:43 But there could be like repeated strings.
But we also. But we have dictionary for the whole thing. Okay, yes, because this is this, would this value would. Still, this value is still in a separate table index table. Okay.
Florian Lehner 00:17:04 Just one thing that comes up in my head.
Jonathan Halliday (IBM) 00:17:07 Have said, it's in 32, and it's not. It's any value.
Yeah, okay, I see what you're saying. Do we want any values to be a lookup table in their own right. I don't think we do.
I think I've miss expressed my intent. There.
Alexey A 00:17:24 Oh, and it says, yes, it shows us in 32, any value. Value. Yes.
Jonathan Halliday (IBM) 00:17:29 Yeah.
Alexey A 00:17:29 Only one.
Jonathan Halliday (IBM) 00:17:30 The data type is any value. It's not my theory.
Alexey A 00:17:34 Yeah.
Jonathan Halliday (IBM) 00:17:35 Edit.
Yes, that's just inlining the the data type. There we go, pushed an update to that.
Yes, I don't think that's worth having off into its own, because the values are going to be different for each one. So we're not going to save space by having a.
Alexey A 00:17:55 Right.
Jonathan Halliday (IBM) 00:17:57 Dictionary.
Florian Lehner 00:18:06 Okay, cool. Then, if there are no other comments on this, I would move on to the next topic.
Topic number 2. Alexei, write a profiling signal proto consistency check.
My last understanding was, we ask for a repository. For this the post.
Alexey A 00:18:31 And also.
Florian Lehner 00:18:32 Information.
Alexey A 00:18:34 Yeah, there, there is a repo request I started working on it. Just in my personal repo.
There's still there's still quite a bit of work to do. But just link it.
Where are the notes here?
Oh, good.
So this is. This is the. It's it's very much beginning. It's there's like I. So I basically, I started to.
I looked at what we have in the collector. And this is recreating some of that. But on top of the proto directly rather than the P data.
there are some like simple checks, but I still need to add tests. And also there is a number of I think, like also, at some point, we will. I will need to decide how deep we want to go in the validation, because there's 1 thing like basic checks, such as, oh, like all indices are within the range of the arrays.
And that's that's kind of easy. Then one like a check. That I also need to add, is the shape of timestamps, because we have certain restrictions on like how Timestamps and values can be can be shaped. That's something we changed recently. But then there is this bigger question of I think I would like to also check, for example, that all call stacks are unique.
or when we or like when we have the function function table, that we don't have duplication because, like things should be, things should be unique by value essentially.
And then this is where I also filed the the issue that Felix commented on is which kind of attributes we're going to support. Like, are we going to support complex attributes? Because.
like, when I start adding uniqueness checks, I will need to decide how to actually check that uniqueness and attributes is one of the. I think this is going to be one of the pains if we want to support complex. No, not pain. But it's just like it will be more complex code. And I want to understand how complex the code should be.
because if we say like attribute can be basically like Json.
then I need to check it recursively and also figure out how to like. Probably like, have a hash table by digest or by full. Well, I don't know. Like I I still have to work to do. One practical question I have is what kind of attribute values we want to support. Do we only want to support simple types which is like primitive types plus homogeneous arrays of primitive types? Or do we want to support complex types, which is what open telemetry seems to be leaning to.
So if anyone, if anyone has any opinions, please speak up.
Florian Lehner 00:21:52 I think I would argue that we could just start with the simple types. Building on this further on is just.
I think that if you start with the simple types, we can still continue later on with complex types.
so it would just help us validate the basics at the moment, and then we can get more into details.
Interesting? What other people think about this.
Alexey A 00:22:23 Yeah. I wonder what Josh thinks? Because the otap for, like this recent Otep for complex types, it does mention profiling. And it says, like, oh, profiling is going to support complex types. I don't know if anyone asked profiling whether whether profiling wants to support complex types. But the Otep does say that.
Josh Suereth 00:22:42 Yeah. The motivation of that Otep is is mostly around trying to figure out what the hell is an event going forward, and then the ability to translate events into other signal types. So if we start from the foundation of like, everything is a complex type as an event, and I need the ability to take an event and open telemetry, turn it into a metric or or place pieces of it in span. How does that work span did not have complex types at all. So the main aim of that Otep was to address the fact that we're starting to put complex types into span because we needed to get events into spans, and we need to get complex types into span events. I should say so. We have compatibility with our new event. Api, and spans The way I would answer that for for you is, I do think, that that way forward was highly contentious, and not a decision made easily. If you look at how long that Otep lingered, for the Otep still calls out that we do not expect complex types in entities like resource attributes, that we do not expect them in metrics, because it actually like metric systems, would really struggle with that. I think it would be fair for you to ignore what the Otip said about profilers, and make your own decision about, hey? In profiling we're going to rely on Simple, for now the reality, though, is that the reason that's happening?
Sdks, that will provide data and produce data did not want to support 2 different like true types, if you will, for attribute and complex attribute or simple attribute and attribute. So they're going to allow attribute to be provided in the Api wherever you would do that.
I don't know if that affects profiling as much, because I don't know if profiling has an Api that users will engage with to produce new data.
So I don't think this will actually impact you the way it impacts like events, logs and metrics.
It might impact resources. But we already said, resources only have simple attributes. So long winded way of saying, I think the proposal of going with simple attributes is probably okay.
but the warning and the the the message of that Otep is, we're not like the we're not requiring simple attributes now.
So somebody might actually produce something that has complex attributes in areas. You would have expected simple for the purpose of of building out like this protocol and everything you're doing. I don't think it changes what I don't think it changes profiling.
But with that context, hopefully, that helps answer.
Alexey A 00:25:31 Thank you. I see Felix.
Felix Geisendörfer 00:25:34 Yeah, just want to quickly respond to does profiling have an Api. We have not started to work on standardizing anything there yet. But I think we will need an Api to set custom attributes from open telemetry sdks to well set trace and span ids, but also, like really user defined attributes go has people off labels for that purpose. But there are very simple type right now. They're basically key value pairs where keys and values have to be strings.
And I don't foresee us wanting to necessarily support complex attributes there, but that that would be the area where we would. We'll probably at some point want to standardize an Api later on.
Alexey A 00:26:19 Okay, then, any objection, if we record. For now that we start with simple attributes that includes homogeneous arrays, I assume, because that's how. That's how traditionally open telemetry defines simple attributes. And I will add this to the documentation. And I can make that assumption in my code.
Florian Lehner 00:26:40 Yeah, thank, you sounds good.
Alexey A 00:26:44 Yeah, I I have another question. But Josh feel free to go ahead.
Josh Suereth 00:26:49 This is. This is in comment to something Felix said. So the the notion that you have labels and Pprof that you're attaching to signals. I'll add an agenda item for this. But we're having a discussion. Semantic conventions. I actually am curious. Why, why, you would do that on the profiling signal, and not on the resource that the profile is attached to.
I'm trying to understand. If, like, this is something people allowed that would have been resource attachments in open telemetry. If you had redesigned it from scratch.
or if it's legitimately like something different than what we allow with resource detection. So again, I'll put this as a separate task or a separate agenda item. I want to walk through it, just calling out that like, Let's discuss that, Alex. I think your your question is probably more important.
Alexey A 00:27:34 I don't know if it's more important, but it's different. I have a question about go, generated Code Repo, because when I was writing code. I figured that actually what we have in the go generated code repo.
It's still old. I think it's like from May or something. For example, the I think, mapping mapping pointer from location, there is still optional. So basically, it's by pointer, not by value. Is there like some automatic process where the go, generated Repo generated code repo just gets updated once in a while, or do I need to do something like, ask someone or do it myself, or what.
Florian Lehner 00:28:24 I think that's the tricky part that we are. Have a lot of changes in the protocol. And there's not always a release on it. And we do have the same issue with Hotel Ebp profiler and all the Otep stuff that is happening in open collector and collector contract because they are still on 1 7 0. And there is No. 1 8 yet, and we have made some significant changes, not breaking changes, I would say. Not like the last one but significant changes in the terms of optional fields we removed some fields as well, and we also have some open prs, so from my experiences is that generating a custom proto 1, 8, or 1 9 with the most recent changes is not an easy task and is heavily involved.
But maybe we can ask someone to make a release of auto proto so that we can trigger the change in open telemetry.
so that we get a newer version.
Alexey A 00:29:43 I can file a bug in that repo just like stating the problem, and probably the the maintainers of that repo will see the bug and and say something.
Florian Lehner 00:29:54 Yeah, that could be an option here.
Then coming back.
Any words on this topic. Otherwise I will continue.
Alexey A 00:30:13 No, that's I. I yeah, I will continue the work, but that's it, for now.
Florian Lehner 00:30:17 Okay. Otherwise. I think there is no news on the review of the benchmarks from Kristos Christos is not able to join today. But I think I did not notice any feedback on this in the last, since we last met.
Otherwise next topic in the active action items. Is Felix with getting simple stack traces? Id, did you find time to update the Pr.
Felix Geisendörfer 00:30:43 I, I did. Yeah. In fact, just before the meeting I updated the Pr description and made it ready for review.
I think this is also gonna tie into crystals benchmarking, because I sort of pointed out one perhaps somewhat surprising result from the benchmarks that my proposal hinges upon is that Alexis double array encoding wins significantly prior to compression. Like, it's 12 and a half percent more efficient. But then, after compression, it actually comes out worse than what we have today by 9.8%, which is pretty surprising. So I think that basically refuse should hone in on this anomaly and and see if if Crystal's benchmark there is is right? Or if yeah, maybe some assumptions could be challenged. But yeah, otherwise, basically, my proposal boils down to Hey, look, we've got these 3 different ways of doing it. There is no clear winner here in terms of like overall like absolutely the best. Because, yeah, I, I think actually, the the current and my proposal are pretty much the same when it comes to efficiency both uncompressed and decompressed, and Alexis is sort of like a mixed back where.
prior to compression, it looks good, and then, after it looks bad, which is probably a trade off. We don't want to do because we really care about post compression, size, and because of that, ultimately, simplicity should be the guiding principle, and that's why we should go with my proposal. That's the summary I I made like another sort of attempt at like spelling out. What's these fancy encodings, or trying to do by making an example of which kind of program might produce stack traces with a lot of prefix repetition. So it's clear to everybody what we're talking about. But yeah, I think it's ready for review. And hopefully we can come to an alignment on this soon. I think we have had like soft buy-in of going this direction. But now I think it's in a good shape to like go through the official review, and we can get it on the way.
Florian Lehner 00:32:46 Okay, thank you. Felix Alexey.
Alexey A 00:32:49 It would probably be good to merge this stack change in particular before like, if we ask someone to cut 1.8, it would be good to include it, because it's because I assume you will also remove the location slice fields.
Felix Geisendörfer 00:33:06 Yes, correct. I think one thing we could also do like just agreement between this group here is the switch from the current ddop algorithm to the stacksing really doesn't change efficiency. So I don't think there's any reason not to do that right now, and it doesn't fully preclude us from like reevaluating the race if we like. See something in crystals, benchmarks that make us reconsider right. I think we're have pretty good reason to believe that we're not going to requests on on performance if we do this. So if we wanted to do it faster under that premise that we were still gonna be willing to to look, take a double look at the race. That might also be a way to go here.
Alexey A 00:33:50 Yeah, I think it's I think it's fine. It's like, well, it's v 1 development repo. After all, I would expect that we can change things back and forth as much as we can. Of course people started to rely on the Api on the, on the proto scheme already.
but it should not come as a surprise that this might break people.
Felix Geisendörfer 00:34:07 Yeah, I I think we have Francesco here, and maybe he was working on the Prof. Wait. What was it? Async profiler recently announced support for open telemetry.
That's that was cool to see.
Florian Lehner 00:34:21 Yeah, great. But, Francesco, and speaking about breaking stuff I think our changes in the protocol did break telegraph. I think that's what's Alex A was referring to?
otherwise. Please. Everyone take a look at the Pr. From Felix. Felix. Thank you for bringing it in and working on this if there's nothing else, we have a lot of agenda. That's why I'm pushing a little bit. next topic would be the hotel SDK communicate process.
I don't see naive in the meeting.
Felix Geisendörfer 00:35:02 No, he's on vacation.
Ivo Anjo 00:35:06 Yeah, he comes back tomorrow. So still, on vacation.
Florian Lehner 00:35:10 Otherwise, if there is a design document you want to discuss, I think we can also discuss this of asynchronousically. Sorry. Yeah. So yeah, happy to see the work on this and if there are no comments on this, then I would continue with 2 topics. I have the ad symbolization attributes to the semantic convention. If you have some time, please have a look.
and also the changes to the protocol removed. Has fields would also need some more approval. So if you have time, please take a look and review. I think there are no open discussions on both sides.
It would bring us further bringing down the rundown list a little bit greener.
Okay, I think that's concludes the active, active action items, and we can continue with the 1st agenda item, the 1st real agenda item. And it's Alexei with the profiles, dictionary and mapping table. Actually, do you want to.
Alexey A 00:36:24 I I think it was. I think it was discussed offline.
yeah, I noticed that we for mapping table and for link table and for string table. We require this like, we have this special meaning for item at 0 index, but not for allocation table function table. And then Christo said.
We don't have optional values there, so that's probably fine.
But then there is a comment. The decision was from Jonathan. Decision was for all dictionary fields to have it.
Oh, but then we decided right. And that that's related to the attribute unit discussion Jonathan, can we split at least like. For example, if we decide, did decided this for function, and.
Jonathan Halliday (IBM) 00:37:15 Yeah, we we could just split the Pr and go back to having a very simple Pr just for the dog comments. But I think we've now reached agreement on the units thing so that should merge, anyway. Do you still want it separate just for tracking purposes?
I've got to fix up.
Alexey A 00:37:32 Mostly mostly just to like if some things are non controversial to get in, I think it's.
Jonathan Halliday (IBM) 00:37:36 Yeah. So when I'm updating that Pr, I'll back out the comment change and I'll raise a new Pr for the comment change. I think that's the easiest thing.
Alexey A 00:37:43 Okay.
Florian Lehner 00:37:46 Okay, thank you.
Alex. Say.
Alexey A 00:37:50 Yeah. Yeah. The next. The next item is actually related to this as well. This is. And this is, it was interesting that Christo's wrote it down because I had like, when writing the the the check, the the the code to check the pro the protos. I had the same question if we don't have any links in the profile which I think is going to be fairly common case.
Florian Lehner 00:38:19 Okay.
Alexey A 00:38:20 Do we still expect to do? We still need to have 0 element, because because samples they will have like default value, which is 0 in the link in the link field like, do we want to special case? The case of like link indexes 0, and the table is empty and allow it, or all producers should still have, like one entry link table with empty element.
Felix Geisendörfer 00:38:52 I would go for the letter. I I think if we do want to have this convention consistently, I think then, yeah, even in this case there should be a empty 0 value in the dictionary table, even if nothing refers to it.
because I mean implicitly, you are referring to it like, because 0 is the default right?
Right? And he's something refer to it.
Alexey A 00:39:13 i i i probably agree.
because that was the decision. And we should. And it's like it's. And it seems like the cost of following, the decision is.
is fairly minor.
Florian Lehner 00:39:33 I just tried to write it on that. We want to have some consistency, and keep the 0 value.
Alexey A 00:39:41 Yes.
and links is probably the only example where this kind of like stands out, because for all like, it's hard to imagine profile with like 0 functions, or 0 lines, or 0 like 0, like no mappings at all.
Well, no mappings, maybe.
Florian Lehner 00:40:05 40 people.
Alexey A 00:40:06 Maybe, like Java, or like man-man, managed languages.
Florian Lehner 00:40:17 Yeah, at the moment. I also cannot think of special cases. I could think of, maybe native code, that where where there is no function, information available.
Alexey A 00:40:31 And oh, it's not symbolized yet.
Florian Lehner 00:40:32 Yes.
Alexey A 00:40:34 Yep.
Florian Lehner 00:40:36 That's that's 1 use case I could think of but this also mean that we don't have a line information at the moment when we don't have symbols, information.
Alexey A 00:40:55 Right.
But then but then you should have like 0. Line, element and line will have 0 function index. So you still, you still need to have that.
Oh, line is line is array. So right line is actually.
Florian Lehner 00:41:11 This could be.
Alexey A 00:41:13 Line, is there? So if you have Z. If you have empty array, then you don't have any references to line.
Florian Lehner 00:41:19 Yeah, right? Right? Yeah.
right? Yeah. Link is, I think the only one that is not an array. If I look.
yeah, Link is just an a regular in 32 index, and the only one that is not an array that links to the tables.
Alexey A 00:41:43 Also mapping mapping is also not on the right, because mapping is from location. So in theory, you could in theory, like you have a Java profile that doesn't set any mapping which would be like 0 index and mapping table would have just entry with with empty mapping.
Florian Lehner 00:42:02 Yes, yes, yeah, that would also be a case. Yeah.
Yeah.
But to conclude, I think there's no to conclude, I think, the agreement is, I would say still, that we meant to to have them con to have consistency between the dictionaries. We keep the serial. Okay.
Alexey A 00:42:23 Christos. Maybe when you update the comments, maybe, would it make sense to call it out specifically that, like this includes the like, the edge case of like. There's at least one item I don't remember if you have this kind of like this. If we we or your Pr have this specific node that basically, this table is never empty.
Florian Lehner 00:42:50 I don't know of a Pr. From Chris Toss, but maybe it can be part of.
Felix Geisendörfer 00:43:00 Yeah. Christas is not here. Lexi
Alexey A 00:43:03 Oh, sorry! I think I meant Jonathan.
Felix Geisendörfer 00:43:05 Oh!
Alexey A 00:43:08 You are updating. Yeah, I think this is. It's it's your pull request.
Jonathan Halliday (IBM) 00:43:14 Yeah, yeah.
Alexey A 00:43:15 For for updating the comments for do we have a comment there that, like basically like, this table is never empty.
Florian Lehner 00:43:30 I think we don't have at the moment. Maybe Jonathan can add it just with the Pr.
Jonathan Halliday (IBM) 00:43:37 Yeah, I think that would make sense.
Alexey A 00:43:39 Okay.
just to call out this special case of like, even if there are no links, there are still like, there's still implicit reference through 0 index sometimes, and so one entry is expected.
Florian Lehner 00:43:57 Yeah, I think this also makes it easier to protocol validation to quantify. If if something that is incoming is valid, if we have, like some kind of consistency, and not special cases for each kind of varied table between the dictionary. So I think that's a good one.
Otherwise, if they're not comments on this, I would go to the next topic.
also on your alexate drop attributes. Count Field.
Alexey A 00:44:32 Yeah, we have this field. I'm just curious, like, what are the exact semantics.
And do we relay? And I see, Jonathan added some comments there config myself.
Yeah. But what is what exactly this is counting? Is this like counting any attributes in any of the entities? Because there are like multiple place where we have attributes. So.
Florian Lehner 00:45:11 I just can add my comment on this quickly, I think dropped attributes. Count is something we got over from the Google, Prof.
Without questioning.
Alexey A 00:45:22 No, no, people doesn't have that field. That's.
Jonathan Halliday (IBM) 00:45:27 No, it's something.
Josh Suereth 00:45:29 Inherited from the other thing.
Jonathan Halliday (IBM) 00:45:31 Which allow you to configure processes to drop attributes based on some criteria like this. Name's too long. I don't want to waste space on it.
Florian Lehner 00:45:42 Okay, then I'm remembering wrong, and maybe Josh can jump in.
Josh Suereth 00:45:46 Yeah, there's there's a general open telemetry. SDK feature where you can set the length limit of attributes.
That length limit means that if an attribute is too long. It gets truncated or or just dropped so like you can end up with reporting. Hey? We dropped these and attributes because someone tried to make one that was too large for your configured default.
There's been some discussion, because that feature doesn't work well with complex attributes. It literally. If you, if you look at the Otep around complex attributes, you can see a discussion between Ludmilla and I on this.
I think if you're trying to match opentelemetry conventions, having dropped attributes, makes sense because we have it everywhere else we have attributes, and there's a general feature that applies to all attributes blanket.
I don't think it's providing users what our goal was, which was. You can fix the size of your telemetry so you don't expand beyond by accident with unknown instrumentation.
But that's that's why it's there. So every single signal in opentele entry has a dropped attribute count every single one that's the design and the goal of it. But with the caveat that if you run into issues with it, you're not alone, and we need to sort some things out with that feature of Otel.
Alexey A 00:47:08 Yeah. And since we use dictionaries, for example, what if I have like if I have 1,000 samples that all reference, one attribute, and that attribute got dropped.
Is it one? Do we count it as one, or do we count it as 1,000.
Josh Suereth 00:47:22 Yeah, you're the 1st signal to have dictionaries. So that would that would. That would probably be a dropped attribute. But I think it also makes the your whole instrumentation somewhat awkward. Right?
anyway. If you keep it.
I think we need to be very explicit about what it means. Is it anytime you saw an attribute? You dropped? You just flip that number, and so the number would be all 1,000, because it never made it into the dictionary.
because otherwise, like, think about this. If you don't drop it on the way to the dictionary, it means you actually have to store it to know you've seen it before, to only report it once so like by by definition dropped attribute. Count is something where, when someone gives you an attribute.
you count, that you dropped it and ignore it because it's too big.
I'm of the opinion, though, that it's almost too late at that point, because they've already taken the memory for the stupid thing in your hot bath. But that's like a different story in question, anyway. Go ahead, Felix.
Felix Geisendörfer 00:48:23 Yeah, I was just going to say the question you brought up whether we should count the chopped attributes that's referenced a thousand times one time or a thousand times, I think you later hinted at it as well. I think the answer is a thousand times it should be the same as if we didn't have dictionary tables like the logical representation, should be the guiding principle.
Alexey A 00:48:42 Right it can be.
I don't think it's impossible. It's just like it can be non trivial because you, it might be like a reference from multiple places in theory, from from multiple entities. Then you need to sum that up and and things like. So like the tracking, the proper, the proper count can by itself be an exercise. I think also, technically, if you drop the attribute, then the samples might be not unique anymore. And technically, you might need to remerge things if we enforce uniqueness anywhere, at least, for example, like, if if collector, let's say, like in the collector somewhere, we check that things are like unique enough. Then, if you remove some attribute, you essentially reduce the cardinality potentially sorry. I don't want to dig this rabbit hole too deep, but it's just like profiling specifics, I think. Make this a bit trickier than maybe, for other signals.
Florian Lehner 00:49:47 I also agree that it become really tricky if we remove an attribute from the dictionary.
or just set it to serial value because we don't know which profiles or which elements in the further down messages reference. This attribute.
This can be in message, profile, message, sample, whatever. And as we don't have an idea where this is referenced.
I think this can introduce a a lot of issues besides. Who accounts for it?
Felix.
Felix Geisendörfer 00:50:31 Yeah, I mean, I guess there's 2 ways this could be implemented. One is, you have some codes that lets you walk all the places where attributes are used. So you can do that without writing very gnarly code. Every time you have this use case, or 2 we could just overwrite that attribute in the dictionary with the empty value essentially right, and still count it as a dropped attribute. Maybe that's a pragmatic way to do it.
Josh Suereth 00:50:57 The the intention here is when someone tries to provide you that attribute, you drop it on the floor like again. If you think about this as the open suntry Api. This is like users giving you attributes, not attributes. You're independently making right. And so the intention is, anytime. Someone tries to give you an attribute that's too big, or would blow out the storage of the SDK. Based on like a convention or parameter. You drop the attribute record that you dropped it, and you just never include it with the original data.
That's how the rest of the open telemetry api specification works.
Felix Geisendörfer 00:51:30 Let me ask something there, because I think I had a different use case in mind, actually, and I thought it exists for the other signals as well. What about redacting information that you don't want to send beyond a collector? So the collector is the one doing the dropping based on privacy pii considerations.
Josh Suereth 00:51:46 Yeah, there's there's a different. That's a good question. That's a different behavior. So I think.
yeah, you can use dropped attributes for that use case. If I recall correctly some of the use cases I've seen there actually keep the original attribute with a redacted like label. So it depends on whether you want to keep a sentinel value. Right? That says, Hey, I know that this had a value. I just redacted it versus not having it at all. I think both. The collector has a general purpose, transformation, language thing that lets you do whatever the hell you want, and half the people that do that don't even update dropped attribute counts by default when they drop attributes. So it's a little bit of a anyway. It's a little bit of a mess right now in the open ecosystem here. But that's a good use case, and I think you should look at how you want to handle that. I might handle that different.
I'm trying to explain to you why dropped attributes exist. In the 1st place, it was a way to protect sdks. It's a general purpose. I can define a size limit. If someone tries to give me a string that's too large, I can reject it, and we allow users to configure. How big that is!
How that applies to profilers, I think, is up to y'all to figure out what you want to do. The dropped attributes. Count was just a way to report it across all signals. If you want to use it for other use cases we can talk about that. Redaction is something we might want to more formalize a noteel, or at least provide guidance. Because again, I think it's a little chaotic. Anyway.
Felix Geisendörfer 00:53:22 Like.
Florian Lehner 00:53:27 Alexei.
Alexey A 00:53:30 It somewhat feels like this comes from some signal where attributes were kind of like the main payload carrier.
because in case of profiling like it's unclear to me. Why attributes are special, for example, compared to stacks? Because if I would want to limit the payload size, wouldn't I want like instead drop like stacks, because we also have strings and stacks are full of strings. That also can also be long. It's unclear to me like, why would I limit the length of strings and attributes, but not in stacks, so I don't. I like I I think it's fine to leave the field, but maybe we want to add a comment that we don't really know yet fully what exactly this means and what the semantics are.
Florian Lehner 00:54:18 Yeah. If if we keep it, I would suggest to move it, not to move it from message profile into the message profiles dictionary, because we want to maybe count with the dictionary attributes that we dropped an attribute rather than having every profile have having this attribute. So maybe we just have to move this field to the dedicated dictionary.
And this would, I think, would also make it easier for for accounting that if you if you say, Hey, I dropped an attribute and this is the account. This is the number of how often it happens. Jonathan.
Jonathan Halliday (IBM) 00:55:03 I'm not sure I agree with that, because I think the the processing pipelines are more likely to be configured, described in terms of the the data model as it exists before the dictionary encoding is applied.
Florian Lehner 00:55:19 Yes, but.
Jonathan Halliday (IBM) 00:55:21 The captain attributes would not be doing it on the dictionary, because it wouldn't be like dictionary aware.
Florian Lehner 00:55:26 Yeah. I just. I'm working on this in the auto collector part.
We have at the moment a very gentlemanly agreement that deleting attributes does not happen.
Jonathan Halliday (IBM) 00:55:38 But it's a gentleman agreement. It's not enforced in any way.
Florian Lehner 00:55:43 And if you're working on a message, sample, message, profile, and all these messages have access to attributes, then you have to have access to the dictionary as well. So this makes it complex. And if you say you update in message sample and attribute, then this would have an impact on the on the dictionary. But you don't walk all other profiles and other messages or samples. That could reference this attribute.
So this is at least, that's what hotel collectors at the moment doing with our hotel.
Jonathan Halliday (IBM) 00:56:24 Redaction filters are also really really hard, because if you configure them without dictionary awareness.
you can potentially have 2 paths by which a value winds up in the dictionary, and the filter applies on only one of them.
and you have to decide whether that means it gets dropped or not.
What that, what that means for information potentially escaping when you don't want it to.
I was thinking about the counting bit as well, and wondering, is there any use for actually knowing exactly how many attributes have dropped? Or can we just have a Boolean? So if we drop an attribute, we replace it, for example, with an attribute that says, this thing has dropped attributes, equals. True?
Is it enough to know that there is missing data? Or do you have to know how much missing data there is.
because, from a point of view of the dictionary encoding, it's a hell of a lot easier to to have a Boolean flag than it is to try and count things and make sense of the the semantics of the Count.
Florian Lehner 00:57:32 Yeah. I see that point. I don't know how it, or if it would conflict with the hotel SDK, in this case.
I would totally favor your approach for simplicity.
But I cannot tell the impact on it.
Josh Suereth 00:58:04 I think we understand the shape of the problem now. I do have to drop in 3 min or 2 min. Apologies. But I would say that this like, in terms of how you want to interact with dropped attributes and how you want to deal with memory bounded profiling right. That's the that's kind of the the thing I would think about.
it is okay. I I'll have to run by the technical committee a little bit. I think it's okay for you to remove the field from Otlp.
for now, if you're not going to use it.
and to think through the concept of like a resilient profiler or a memory bound profiler, and figure out, what do you need in the protocol to communicate where you ran into memory bounds and had to make decisions based on shrinking things. Right?
As a, as a team, as a group. And then we can, we can update the protocol for the support that you need there. Right? So I I think that it was a great discussion. But I don't think we have a handle on the solution right now, nor do I think another like 5 min will fix it. So I think it's something to kind of think through and and divide as a group, but in terms of the overall open telemetry conventions here you definitely convinced me that I don't think. Just attribute drop count is enough, or fits well with what you're doing in profiling. So let's sort out what we need to do and why it has to be different the same way the dictionaries were like proposed. Right? I think it's it's a similar evolution there. But yeah, let's let's figure out what what does safe, you know, memory bounded, profiling look like that. That would be the I'd rather focus on that discussion than specifically dropped. Attribute Count.
Florian Lehner 01:00:01 Yeah, thank you for this words, Josh, and we are running out of time. So 20 seconds left, and we have a still full agenda ahead of us.
I think there are no time left for big comments. If you have something that's really urgent, speak up now. Otherwise I'm asking you to write in the slack channel. And again the items we did not touch. Today I will move to the next meeting. So in 2 weeks. And yeah, asking everyone again to have a look at the Prs that we have open. There are a couple of things.
and I think we can ask more for 1 8 release. If we have to merged, it will bring us a big step for further further. Otherwise. unfortunately, our time is out now.
So I guess. Thank you. Everyone for your time, and sorry if we didn't manage to talk about your topic. Felix. Last words.
Felix Geisendörfer 01:01:03 Yeah, I had a very short one just to prime people thinking for next time, I think we should consider doing a release candidate one or 2 before we publish 1.0, basically, once we think it's like stable enough so that implementations can do some testing. Everybody, maybe just think about this until next time.
Florian Lehner 01:01:21 If you're talking about Rc. One for the protocol or.
Felix Geisendörfer 01:01:25 Protocol.
Florian Lehner 01:01:26 Okay, okay, okay, cool.
Yep.
Cool.
Otherwise the church bells in my background are ringing. We are out of time. Wish you everyone good local time. And thanks for everyone.
Felix Geisendörfer 01:01:43 Everyone has to.
Alexey A 01:01:44 Feel like it's get better.
Florian Lehner 01:01:48 Yeah, thank, you.
Felix Geisendörfer 01:01:49 Okay. See? You.
